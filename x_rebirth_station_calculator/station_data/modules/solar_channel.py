from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Solar Channel',
         'L049': 'Solar-Tunnel'}

productions = {'dv': [Production(wares.EnergyCells, 8400)]}

consumptions = {'dv': [Consumption(wares.FoodRations, 48.0, True)]}

SolarChannel = Module(names, productions, consumptions)
