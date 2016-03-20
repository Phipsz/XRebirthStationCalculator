import modules
import wares
from ..station_base import Station
from ..station_base import Production
from ..station_base import Consumption

names = {'L044': 'Solar Energy Farm',
         'L049': 'Solarkraftwerk'}

smodules = [(modules.SolarChannel, 4)]

productions = [Production(wares.EnergyCells, 33600.0, 152.0)]

consumptions = [Consumption(wares.FoodRations, 192.0, True)]

DV_SolarEnergyFarm = Station(names, smodules, productions, consumptions)
