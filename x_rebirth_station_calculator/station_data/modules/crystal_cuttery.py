from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Crystal Cuttery',
         'L049': 'Kristallschleiferei'}

productions = {'al': [Production(wares.CutCrystals, 2640)],
               'ar': [Production(wares.CutCrystals, 2640)]}

consumptions = {'al': [Consumption(wares.Crystals, 1400),
                       Consumption(wares.EnergyCells, 1920),
                       Consumption(wares.FoodRations, 1440),
                       Consumption(wares.Water, 960),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 24, True)],

                'ar': [Consumption(wares.BoFu, 720),
                       Consumption(wares.Crystals, 2400),
                       Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.Water, 960),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 24, True)]}

CrystalCuttery = Module(names, productions, consumptions)
