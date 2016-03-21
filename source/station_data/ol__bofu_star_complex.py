from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'BoFu Star Complex',
         'L049': 'BoFu-Sternenplex'}

smodules = [(modules.BoFuKitchen, 4)]

productions = [Production(wares.FoodRations, 25920, 155.0)]

consumptions = [Consumption(wares.EnergyCells, 12960.0),
                Consumption(wares.Plankton, 20160.0),
                Consumption(wares.SoyBeans, 10080.0),
                Consumption(wares.Spices, 7200.0)]

OL_BoFuStarComplex = Station(names, smodules, productions, consumptions)
