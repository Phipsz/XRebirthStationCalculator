from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'High Tech Fab',
         'L049': 'High-Tech-Fab'}

smodules = [modules.ChipFab(production_method='al', efficiency=152),
            modules.ChipFab(production_method='al', efficiency=140),
            modules.BioOpticsFac(production_method='al', efficiency=141),
            modules.BioOpticsFac(production_method='al', efficiency=144),
            modules.ScannArFacility(production_method='al', efficiency=141),
            modules.ScannArFacility(production_method='al', efficiency=145)]

AL_HighTechFab = Station(names, smodules)
