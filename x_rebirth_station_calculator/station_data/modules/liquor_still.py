from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Liquor Still',
         'L049': 'Krautdestille'}

productions = {'al': [Production(wares.Spacefuel, 1920)],
               'ar': [Production(wares.Spacefuel, 960)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 960),
                       Consumption(wares.Spices, 480),
                       Consumption(wares.Water, 1920),
                       Consumption(wares.Wheat, 240)],

                'ar': [Consumption(wares.EnergyCells, 480),
                       Consumption(wares.Plankton, 120),
                       Consumption(wares.Spices, 240),
                       Consumption(wares.Water, 960)]}

LiquorStill = Module(names, productions, consumptions)
