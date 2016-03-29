from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'BoFu Kitchen',
         'L049': 'BoFu-Küchen'}

productions = {'ar': [Production(wares.BoFu, 2160)]}

consumptions = {'ar': [Consumption(wares.EnergyCells, 1080),
                       Consumption(wares.Plankton, 1680),
                       Consumption(wares.SoyBeans, 840),
                       Consumption(wares.Spices, 600)]}

BoFuKitchen = Module(names, productions, consumptions)
