from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Floating Meadows',
         'L049': 'Gravitationsweiden'}

smodules = [modules.ValleyForge(production_method='al', efficiency=147),
            modules.ValleyForge(production_method='al', efficiency=147),
            modules.ValleyForge(production_method='al', efficiency=147),
            modules.ValleyForge(production_method='al', efficiency=147),
            modules.ArgnuParadise(production_method='al', efficiency=150),
            modules.ArgnuParadise(production_method='al', efficiency=144),
            modules.SpiceTubes(efficiency=147)]

AL_FloatingMeadows = Station(names, smodules)
