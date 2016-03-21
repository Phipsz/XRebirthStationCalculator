from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Water Distillery',
         'L049': 'Wasserveredelung'}

smodules = [(modules.CondenserStill, 2)]

productions = [Production(wares.Water, 28800.0, 144.0)]

consumptions = [Consumption(wares.Ice, 24000.0),
                Consumption(wares.EnergyCells, 4800.0)]

DV_WaterDistillery = Station(names, smodules, productions, consumptions)
