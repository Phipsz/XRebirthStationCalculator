from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Soy Beanery',
         'L049': 'Sojabohnenanlage'}

productions = {'ar': [Production(wares.SoyBeans, 1440)]}

consumptions = {'ar': [Consumption(wares.EnergyCells, 720),
                       Consumption(wares.Water, 1440)]}

SoyBeanery = Module(names, productions, consumptions)
