from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Cube Plant',
         'L049': 'Würfelfabrik'}

productions = {'al': [Production(wares.NividiumCubes, 2640)],
               'ar': [Production(wares.NividiumCubes, 2640)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 1920),
                       Consumption(wares.FoodRations, 1440),
                       Consumption(wares.Nividium, 2400),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 24, True)],

                'ar': [Consumption(wares.BoFu, 720),
                       Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.Nividium, 2400),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 24, True)]}

CubePlant = Module(names, productions, consumptions)
