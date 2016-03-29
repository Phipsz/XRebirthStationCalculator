from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Wheat Plantation',
         'L049': 'Weizenplantage'}

smodules = [modules.ValleyForge(production_method='al', efficiency=140),
            modules.ValleyForge(production_method='al', efficiency=140)]

DV_WheatPlantation = Station(names, smodules)
