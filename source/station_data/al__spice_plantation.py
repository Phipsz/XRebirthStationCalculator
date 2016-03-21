from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Spice Plantation',
         'L049': 'Gewürzplantage'}

smodules = [(modules.SpiceTubes, 2),
            (modules.HerbGarden, 2)]

productions = [Production(wares.Spices, 6400.0, 145.0),
               Production(wares.Spaceweed, 2400.0, 146.0)]

consumptions = [Consumption(wares.EnergyCells, 2560.0),
                Consumption(wares.Spacefuel, 480.0),
                Consumption(wares.Water, 9600.0)]

AL_SpicePlantation = Station(names, smodules, productions, consumptions)
