from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Arms Tech Fab',
         'L049': 'Waffen-Tech Fab'}

smodules = [modules.PlateFoundry(production_method='al', efficiency=134),
            modules.ScannArFacility(production_method='al', efficiency=134),
            modules.WarheadForge(production_method='al', efficiency=152),
            modules.MissileForge(production_method='al', efficiency=152),
            modules.TurretForge(production_method='al', efficiency=134),
            modules.ShieldFacility(production_method='al', efficiency=131)]

AL_ArmsTechFab = Station(names, smodules)
