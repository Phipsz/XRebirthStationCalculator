from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Energy Array',
         'L049': 'Energiematrix'}

smodules = [(modules.ECellFab, 4)]

productions = [Production(wares.EnergyCells, 67200.0, 150.0)]

consumptions = [Consumption(wares.FoodRations, 384.0, True)]

AL_EnergyArray = Station(names, smodules, productions, consumptions)
