from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'BoFu Star Complex',
         'L049': 'BoFu-Sternenplex'}

smodules = [modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158),
            modules.BoFuKitchen(production_method='ar', efficiency=158)]

OL_BoFuStarComplex = Station(names, smodules)
