from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Bio-Optics Fac',
         'L049': 'Bio-Optik-Anlage'}

productions = {'al': [Production(wares.BioOpticWiring, 240)]}

consumptions = {'al': [Consumption(wares.ChemicalCompounds, 320),
                       Consumption(wares.EnergyCells, 960),
                       Consumption(wares.FoodRations, 480),
                       Consumption(wares.PlasmaCells, 320),
                       Consumption(wares.MedicalSupplies, 80, True),
                       Consumption(wares.Spacefuel, 120, True)]}

BioOpticsFac = Module(names, productions, consumptions)
