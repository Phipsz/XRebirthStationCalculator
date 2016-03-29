from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Valley Plantation',
         'L049': 'Talplantage'}

smodules = [modules.ValleyForge(production_method='al', efficiency=150),
            modules.ValleyForge(production_method='al', efficiency=150),
            modules.ValleyForge(production_method='al', efficiency=150),
            modules.ValleyForge(production_method='al', efficiency=150),
            modules.ValleyForge(production_method='al', efficiency=150),
            modules.ValleyForge(production_method='al', efficiency=150)]

AL_ValleyPlantation = Station(names, smodules)
