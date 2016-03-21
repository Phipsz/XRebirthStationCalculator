from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Solar Energy Farm',
         'L049': 'Solarkraftwerk'}

smodules = [(modules.SolarChannel, 4)]

productions = [Production(wares.EnergyCells, 33600.0, 152.0)]

consumptions = [Consumption(wares.FoodRations, 192.0, True)]

DV_SolarEnergyFarm = Station(names, smodules, productions, consumptions)
