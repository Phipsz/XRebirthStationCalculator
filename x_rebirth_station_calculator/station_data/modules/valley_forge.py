from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Valley Forge',
         'L049': 'Talschmiede'}

productions = {'al': [Production(wares.Wheat, 5400.0)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 600),
                       Consumption(wares.Water, 3000)]}

ValleyForge = Module(names, productions, consumptions)
