from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'TechnoCore Parts',
         'L049': 'TechnoCore-Teile'}

smodules = [modules.GelFactory(production_method='ar', efficiency=162),
            modules.GelFactory(production_method='ar', efficiency=164),
            modules.EMFacTower(production_method='ar', efficiency=164),
            modules.EMFacTower(production_method='ar', efficiency=164),
            modules.PPPPlant(production_method='ar', efficiency=164),
            modules.PPPPlant(production_method='ar', efficiency=164)]

OL_TechnoCoreParts = Station(names, smodules)
