from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Tech Laboratory',
         'L049': 'Technologie-Lab'}

smodules = [modules.ChemRefinery(production_method='al', efficiency=149),
            modules.ChemRefinery(production_method='al', efficiency=142),
            modules.ChipFab(production_method='al', efficiency=146),
            modules.ChipFab(production_method='al', efficiency=140),
            modules.BioOpticsFac(production_method='al', efficiency=141),
            modules.BioOpticsFac(production_method='al', efficiency=145),
            modules.QTubeYFab(production_method='al', efficiency=145),
            modules.QTubeYFab(production_method='al', efficiency=145)]

AL_TechLaboratory = Station(names, smodules)
