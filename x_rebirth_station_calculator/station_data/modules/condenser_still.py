from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Condenser Still',
         'L049': 'Kondensator-Anlage'}

productions = {'al': [Production(wares.Water, 14400.0)],
               'ar': [Production(wares.Water, 12000.0)]}

consumptions = {'al': [Consumption(wares.Ice, 12000.0),
                       Consumption(wares.EnergyCells, 2400.0)],

                'ar': [Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.Ice, 9600)]}

CondenserStill = Module(names, productions, consumptions)
