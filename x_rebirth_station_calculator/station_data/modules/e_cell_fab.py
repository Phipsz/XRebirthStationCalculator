from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'E-Cell Fab',
         'L049': 'E-Zellen Fab'}

productions = {'al': [Production(wares.EnergyCells, 8400)]}

consumptions = {'al': [Consumption(wares.FoodRations, 48, True)]}

ECellFab = Module(names, productions, consumptions)
