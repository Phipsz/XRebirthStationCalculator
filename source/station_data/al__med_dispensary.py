from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Med Dispensary',
         'L049': 'Med-Labor'}

smodules = [(modules.PharmaPlatform, 2),
            (modules.NarcoticsLab, 2),
            (modules.HerbGarden, 2)]

productions = [Production(wares.MedicalSupplies, 2880.0, 145.0),
               Production(wares.Narcotics, 2880.0, 144.0),
               Production(wares.Spaceweed, 2400.0, 145.0)]

consumptions = [Consumption(wares.EnergyCells, 3840.0),
                Consumption(wares.Narcotics, 2880.0),
                Consumption(wares.Spaceweed, 4320.0),
                Consumption(wares.Spacefuel, 480.0),
                Consumption(wares.Water, 2400.0)]

AL_MedDispensary = Station(names, smodules, productions, consumptions)
