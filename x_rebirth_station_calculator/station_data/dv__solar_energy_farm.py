from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Solar Energy Farm',
         'L049': 'Solarkraftwerk'}

smodules = [modules.SolarChannel(production_method='dv', efficiency=145.0),
            modules.SolarChannel(production_method='dv', efficiency=145.0),
            modules.SolarChannel(production_method='dv', efficiency=145.0),
            modules.SolarChannel(production_method='dv', efficiency=145.0)]

DV_SolarEnergyFarm = Station(names, smodules)
