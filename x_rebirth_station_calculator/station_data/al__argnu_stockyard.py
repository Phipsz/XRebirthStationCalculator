from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Argnu Stockyard',
         'L049': 'Argnu-Zuchtplantagen'}

smodules = [modules.ArgnuParadise(production_method='al', efficiency=147),
            modules.ArgnuParadise(production_method='al', efficiency=146),
            modules.ArgnuParadise(production_method='al', efficiency=144),
            modules.ArgnuParadise(production_method='al', efficiency=146)]

AL_ArgnuStockyard = Station(names, smodules)
