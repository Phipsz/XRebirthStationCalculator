from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'TechnoCore Hi-E',
         'L049': 'TechnoCore H-E'}

smodules = [modules.FusionCoreFac(production_method='ar', efficiency=152),
            modules.FusionCoreFac(production_method='ar', efficiency=152),
            modules.PodkletnovFab(production_method='ar', efficiency=149),
            modules.PodkletnovFab(production_method='ar', efficiency=153),
            modules.PlasmaTech(production_method='ar', efficiency=152),
            modules.PlasmaTech(production_method='ar', efficiency=146)]

OL_TechnoCoreHiE = Station(names, smodules)
