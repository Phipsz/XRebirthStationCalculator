from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Mil Hi-Tech Manuf',
         'L049': 'Mil Hi-Tech Manuf'}

smodules = [modules.MissileForge(production_method='ar', efficiency=166),
            modules.MissileForge(production_method='ar', efficiency=153),
            modules.TurretForge(production_method='ar', efficiency=135),
            modules.TurretForge(production_method='ar', efficiency=135),
            modules.ShieldFacility(production_method='ar', efficiency=134),
            modules.ShieldFacility(production_method='ar', efficiency=134)]

OL_MilHiTechManuf = Station(names, smodules)
