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
        wares = dict()
        for module in self.modules:
            for production in module.productions:
                warename = production.ware.get_name()
                if warename in data:
                    data[warename] += production.get_production_rate()
                else:
                    data[warename] = production.get_production_rate()
                    wares[warename] = production.ware

        self.productions = list()
        for k, v in data.items():
            self.productions.append(Production(wares[k], v))

    def calculate_consumption_data(self):
        data = dict()
        wares = dict()
        for module in self.modules:
            for consumption in module.consumptions:
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


class Module:
    def __init__(self, name, productions=None, consumptions=None,
                 production_method='universal', efficiency=100):
        self.name = name
        self.productions = productions
        self.consumptions = consumptions
        self.efficiency = efficiency
        if self.productions is not None:
            productions = list()
            for prod in self.productions[production_method]:
                productions.append(Production(prod.ware, prod.amount,
                                              self.efficiency))

    def get_name(self, lang=None):
        if not lang:
            lang = 'L044'
        return self.name.get(lang, self.name)

    def get_module(self, production_method='universal', efficiency=100):
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

    def str_amount(self):
        return str(self.amount.quantize(TWOPLACES))

    def str_production_rate(self):
        return str(self.get_production_rate().quantize(TWOPLACES))


class Consumption:
    def __init__(self, ware, amount, is_secondary=False):
        self.ware = ware
        self.amount = decimal.Decimal(str(amount))
        self.is_secondary = is_secondary

    def get_consumption_rate(self):
        return self.amount

    def str_consumption_rate(self):
        return str(self.get_consumption_rate().quantize(TWOPLACES))
