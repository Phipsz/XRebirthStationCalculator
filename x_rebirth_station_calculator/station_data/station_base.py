import decimal

TWOPLACES = decimal.Decimal('0.01')


class Station:
    def __init__(self, name, modules, productions=None, consumptions=None):
        self.name = name
        self.modules = modules
        self.productions = productions
        self.consumptions = consumptions

    def get_name(self, lang=None):
        if not lang or lang not in self.name:
            lang = 'L044'
        return self.name.get(lang, self.name)

    def sort_data(self, language='L044'):
        self.get_production_data()
        self.get_consumption_data()
        self.productions.sort(key=lambda prod: prod.ware.get_name(language))
        self.consumptions.sort(key=lambda cons: cons.ware.get_name(language))

    def get_production_data(self):
        if self.productions is None:
            self.calculate_production_data()
        return self.productions

    def get_consumption_data(self):
        if self.consumptions is None:
            self.calculate_consumption_data()
        return self.consumptions

    def calculate_production_data(self):
        data = dict()
        base_data = dict()
        wares = dict()
        for module in self.modules:
            for production in module.get_productions():
                warename = production.ware.get_name()
                if warename in data:
                    data[warename] += production.get_production_rate()
                    base_data[warename] += production.amount
                else:
                    data[warename] = production.get_production_rate()
                    base_data[warename] = production.amount
                    wares[warename] = production.ware

        self.productions = list()
        for k, v in wares.items():
            eff = data[k] / base_data[k] * 100
            self.productions.append(Production(v, base_data[k], eff))

    def calculate_consumption_data(self):
        data = dict()
        wares = dict()
        for module in self.modules:
            for consumption in module.get_consumptions():
                warename = consumption.ware.get_name()
                if consumption.is_secondary:
                    warename += ' secondary'
                if warename in data:
                    data[warename] += consumption.amount
                else:
                    data[warename] = consumption.amount
                    wares[warename] = consumption.ware

        self.consumptions = list()
        for k, v in data.items():
            secondary = False
            if k.endswith(' secondary'):
                secondary = True
            self.consumptions.append(Consumption(wares[k], v, secondary))

    @staticmethod
    def get_ware_production_info(stations, language='L044'):
        """This method calculates total production, consumption and their
        difference for a given list of stations. The input list has to be a
        datatype that can be indexed, e.g. using the following datatype:
            stationInfo = collections.namedtuple('StationInfo', ['station',
                                                                 'count'])

        The result will be encoded in a dict with the keys 'productions',
        'consumptions', 'result' and 'list'. 'list' contains all wares (unique)
        ordered by localised name. 'consumptions', 'productions' and 'result'
        contain a dict, where the key is the unlocalised name of a ware
        (ware.get_name()) and the value is the corresponding information. Note
        that not all wares must be present in both, 'consumption' or
        'productions'."""
        from operator import methodcaller
        wares = {'productions': dict(),
                 'consumptions': dict(),
                 'result': dict(),
                 'list': set()}
        for station_info in stations:
            productions = station_info.station.get_production_data()
            consumptions = station_info.station.get_consumption_data()
            for prdctn in productions:
                warename = prdctn.ware.get_name()
                wares['list'].add(prdctn.ware)
                rate = prdctn.get_production_rate() * station_info.count
                if warename in wares['productions']:
                    wares['productions'][warename] += rate
                else:
                    wares['productions'][warename] = rate
            for cnsmptn in consumptions:
                warename = cnsmptn.ware.get_name()
                wares['list'].add(cnsmptn.ware)
                rate = cnsmptn.get_consumption_rate() * station_info.count
                if warename in wares['consumptions']:
                    wares['consumptions'][warename] += rate
                else:
                    wares['consumptions'][warename] = rate
            for ware in wares['list']:
                prod_rate = wares['productions'].get(ware.get_name(), 0)
                cons_rate = wares['consumptions'].get(ware.get_name(), 0)
                result = prod_rate - cons_rate
                wares['result'][ware.get_name()] = result.quantize(TWOPLACES)
        wares['list'] = sorted(wares['list'], key=methodcaller('get_name',
                                                               language))
        return wares


class Module:
    def __init__(self, name, productions=None, consumptions=None,
                 production_method='universal', efficiency=100):
        self.name = name
        self.consumptions = consumptions
        self.efficiency = efficiency
        self.production_method = production_method

        self.productions = productions
        if productions:
            self.productions = dict()
            for prod_method in productions:
                self.productions[prod_method] = list()
                for i in range(len(productions[prod_method])):
                    prod = productions[prod_method][i]
                    new_prod = Production(prod.ware, prod.amount,
                                          self.efficiency)
                    self.productions[prod_method].append(new_prod)

    def get_name(self, lang=None):
        if not lang:
            lang = 'L044'
        return self.name.get(lang, self.name)

    def get_productions(self):
        if self.productions:
            return self.productions[self.production_method]
        return list()

    def get_consumptions(self):
        if self.consumptions:
            return self.consumptions[self.production_method]
        return list()

    def __call__(self, production_method='universal', efficiency=100):
        return Module(self.name, self.productions, self.consumptions,
                      production_method, efficiency)


class Ware:
    def __init__(self, name):
        self.name = name

    def get_name(self, lang=None):
        if not lang:
            lang = 'L044'
        return self.name.get(lang, self.name)


class Production:
    def __init__(self, ware, amount, efficiency=100.0):
        self.ware = ware
        self.amount = decimal.Decimal(str(amount))
        self.efficiency = decimal.Decimal(str(efficiency))

    def get_production_rate(self):
        return (self.amount * (self.efficiency / decimal.Decimal('100.0')))

    def str_amount(self, language='l044'):
        return self._format_amount(self.amount, language)

    def str_production_rate(self, language='l044'):
        return self._format_amount(self.get_production_rate(), language)

    def _format_amount(self, amount, language='L044'):
        from x_rebirth_station_calculator.web.translations import LOCALE_LIST
        import locale
        locale.setlocale(locale.LC_ALL, LOCALE_LIST[language])
        return locale.format('%.2f', amount.quantize(TWOPLACES), grouping=True)


class Consumption:
    def __init__(self, ware, amount, is_secondary=False):
        self.ware = ware
        self.amount = decimal.Decimal(str(amount))
        self.is_secondary = is_secondary

    def get_consumption_rate(self):
        return self.amount

    def str_consumption_rate(self):
        return str(self.get_consumption_rate().quantize(TWOPLACES))
