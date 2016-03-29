from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'URV BTO Line',
         'L049': 'URV-Auftragsfertigung'}

smodules = [modules.URVWharf(production_method='al', efficiency=116),
            modules.URVWharf(production_method='al', efficiency=106),
            modules.URVWharf(production_method='al', efficiency=109),
            modules.URVWharf(production_method='al', efficiency=106)]

AL_URVBTOLine = Station(names, smodules)
