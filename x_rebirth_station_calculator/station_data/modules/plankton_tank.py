from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Plankton Tank',
         'L049': 'Planktontank'}

productions = {'ar': [Production(wares.Plankton, 2880)]}

consumptions = {'ar': [Consumption(wares.EnergyCells, 240),
                       Consumption(wares.Water, 1440)]}

PlanktonTank = Module(names, productions, consumptions)
