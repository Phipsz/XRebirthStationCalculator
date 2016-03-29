from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Solar Converter',
         'L049': 'Solar-Konverter'}

productions = {'ar': [Production(wares.EnergyCells, 8400)]}

consumptions = {'ar': [Consumption(wares.BoFu, 24, True)]}

SolarConverter = Module(names, productions, consumptions)
