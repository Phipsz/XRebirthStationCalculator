from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Techno-Complex',
         'L049': 'Technoplex'}

smodules = [modules.QTubeYFab(production_method='al', efficiency=148),
            modules.QTubeYFab(production_method='al', efficiency=146),
            modules.BioOpticsFac(production_method='al', efficiency=145),
            modules.BioOpticsFac(production_method='al', efficiency=148),
            modules.ScannArFacility(production_method='al', efficiency=145),
            modules.WarheadForge(production_method='al', efficiency=141)]

AL_TechnoComplex = Station(names, smodules)
