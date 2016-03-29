from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Technology Megacomplex',
         'L049': 'Techno-Megaplex'}

smodules = [modules.QTubeYFab(production_method='ar', efficiency=174),
            modules.QTubeYFab(production_method='ar', efficiency=164),
            modules.PPPPlant(production_method='ar', efficiency=157),
            modules.PPPPlant(production_method='ar', efficiency=164),
            modules.EMFacTower(production_method='ar', efficiency=158),
            modules.WarheadForge(production_method='ar', efficiency=158)]

OL_TechnologyMegacomplex = Station(names, smodules)
