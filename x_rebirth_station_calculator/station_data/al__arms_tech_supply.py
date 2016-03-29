from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Arms Tech Supply',
         'L049': 'Waffen-Tech Zulieferer'}

smodules = [modules.MissileForge(production_method='al', efficiency=157),
            modules.MissileForge(production_method='al', efficiency=154),
            modules.TurretForge(production_method='al', efficiency=134),
            modules.TurretForge(production_method='al', efficiency=132),
            modules.ShieldFacility(production_method='al', efficiency=128),
            modules.ShieldFacility(production_method='al', efficiency=133)]

AL_ArmsTechSupply = Station(names, smodules)
