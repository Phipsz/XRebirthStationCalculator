from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'URV Mass Line',
         'L049': 'URV-Massenfertigung'}

smodules = [modules.URVWharf(production_method='ar', efficiency=117),
            modules.URVWharf(production_method='ar', efficiency=115),
            modules.URVWharf(production_method='ar', efficiency=117),
            modules.URVWharf(production_method='ar', efficiency=117)]

OL_URVMassLine = Station(names, smodules)
