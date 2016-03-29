from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Argnu Paradise',
         'L049': 'Argnu-Paradies'}

productions = {'al': [Production(wares.Meat, 1920)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 720),
                       Consumption(wares.Water, 1680),
                       Consumption(wares.Wheat, 1680)]}

ArgnuParadise = Module(names, productions, consumptions)
