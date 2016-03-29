from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Mil Hi-Tech Dept',
         'L049': 'Mil Hi-Tech Abt'}

smodules = [modules.PlateFoundry(production_method='ar', efficiency=161),
            modules.EMFacTower(production_method='ar', efficiency=152),
            modules.WarheadForge(production_method='ar', efficiency=149),
            modules.MissileForge(production_method='ar', efficiency=152),
            modules.TurretForge(production_method='ar', efficiency=133),
            modules.ShieldFacility(production_method='ar', efficiency=135)]

OL_MilHiTechDept = Station(names, smodules)
