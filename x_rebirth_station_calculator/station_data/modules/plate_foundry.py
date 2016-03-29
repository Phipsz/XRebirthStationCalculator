from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Plate Foundry',
         'L049': 'Platten-Fertigung'}

productions = {'al': [Production(wares.ReinforcedMetalPlating, 400)],
               'ar': [Production(wares.ReinforcedMetalPlating, 360)]}

consumptions = {'al': [Consumption(wares.ChemicalCompounds, 480),
                       Consumption(wares.EnergyCells, 1280),
                       Consumption(wares.FoodRations, 960),
                       Consumption(wares.NividiumCubes, 640),
                       Consumption(wares.RefinedMetals, 2400),
                       Consumption(wares.MedicalSupplies, 160, True),
                       Consumption(wares.Spacefuel, 1600, True)],

                'ar': [Consumption(wares.BoFu, 440),
                       Consumption(wares.ChemicalCompounds, 240),
                       Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.NividiumCubes, 640),
                       Consumption(wares.RefinedMetals, 1960),
                       Consumption(wares.MedicalSupplies, 160, True),
                       Consumption(wares.Spacefuel, 1200, True)]}

PlateFoundry = Module(names, productions, consumptions)
