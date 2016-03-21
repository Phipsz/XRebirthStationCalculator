from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Pharma-Spice Farm',
         'L049': 'Heilpflanzenplantage'}

smodules = [(modules.SpiceTubes, 3),
            (modules.HerbGarden, 3)]

productions = [Production(wares.Spices, 9600.0, 159.67),
               Production(wares.Spaceweed, 3600.0, 162.0)]

consumptions = [Consumption(wares.EnergyCells, 3840.0),
                Consumption(wares.Spacefuel, 720.0),
                Consumption(wares.Water, 14400.0)]

OL_PharmaSpiceFarm = Station(names, smodules, productions, consumptions)
