from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'R&D Chem Lab',
         'L049': 'F&E Chem-Lab'}

smodules = [modules.ChemRefinery(production_method='ar', efficiency=185),
            modules.ChemRefinery(production_method='ar', efficiency=161),
            modules.GelFactory(production_method='ar', efficiency=162),
            modules.GelFactory(production_method='ar', efficiency=164),
            modules.PPPPlant(production_method='ar', efficiency=169),
            modules.PPPPlant(production_method='ar', efficiency=164),
            modules.QTubeYFab(production_method='ar', efficiency=170),
            modules.QTubeYFab(production_method='ar', efficiency=176)]

OL_RDChemLab = Station(names, smodules)
