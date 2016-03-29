from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Ship Tech Fab',
         'L049': 'Schiffstech Fab'}

smodules = [modules.FusionCoreFac(production_method='al', efficiency=153),
            modules.FusionCoreFac(production_method='al', efficiency=144),
            modules.PlasmaTech(production_method='al', efficiency=142),
            modules.PlasmaTech(production_method='al', efficiency=140),
            modules.PodkletnovFab(production_method='al', efficiency=146),
            modules.PodkletnovFab(production_method='al', efficiency=141)]

AL_ShipTechFab = Station(names, smodules)
