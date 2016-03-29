from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Med Dispensary',
         'L049': 'Med-Labor'}

smodules = [modules.PharmaPlatform(efficiency=144),
            modules.PharmaPlatform(efficiency=144),
            modules.NarcoticsLab(efficiency=143),
            modules.NarcoticsLab(efficiency=143),
            modules.HerbGarden(efficiency=144),
            modules.HerbGarden(efficiency=144)]

AL_MedDispensary = Station(names, smodules)
