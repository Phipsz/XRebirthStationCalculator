from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Floating Meadows',
         'L049': 'Gravitationsweiden'}

smodules = [(modules.ValleyForge, 4),
            (modules.ArgnuParadise, 2),
            (modules.SpiceTubes, 1)]

productions = [Production(wares.Wheat, 21600.0, 147.0),
               Production(wares.Meat, 3840.0, 147.0),
               Production(wares.Spices, 3200.0, 147.0)]

consumptions = [Consumption(wares.Water, 18960.0),
                Consumption(wares.EnergyCells, 4640.0),
                Consumption(wares.Wheat, 3360.0)]

AL_FloatingMeadows = Station(names, smodules, productions, consumptions)
