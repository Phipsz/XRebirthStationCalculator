class Station:
    def __init__(self, name, modules, productions, consumptions):
        self.name = name
        self.modules = modules
        self.productions = productions
        self.consumptions = consumptions

    def get_name(self, lang='L044'):
        return self.name.get(lang, self.name)


class Module:
    def __init__(self, name):
        self.name = name

    def get_name(self, lang='L044'):
        return self.name.get(lang, self.name)


class Ware:
    def __init__(self, name):
        self.name = name

    def get_name(self, lang='L044'):
        return self.name.get(lang, self.name)


class Production:
    def __init__(self, ware, amount, efficiency):
        self.ware = ware
        self.amount = amount
        self.efficiency = efficiency

    def get_production_rate(self):
        return self.amount * self.efficiency


class Consumption:
    def __init__(self, ware, amount, is_secondary=False):
        self.ware = ware
        self.amount = amount
        self.is_secondary = is_secondary
