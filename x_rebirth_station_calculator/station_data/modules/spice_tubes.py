from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Spice Tubes',
         'L049': 'Gewürzröhren'}

productions = {'universal': [Production(wares.Spices, 3200)]}

consumptions = {'universal': [Consumption(wares.EnergyCells, 800),
                              Consumption(wares.Water, 3600)]}

SpiceTubes = Module(names, productions, consumptions)
