from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Spice Plantation',
         'L049': 'Gewürzplantage'}

smodules = [modules.SpiceTubes(efficiency=144),
            modules.SpiceTubes(efficiency=144),
            modules.HerbGarden(efficiency=147),
            modules.HerbGarden(efficiency=144)]

AL_SpicePlantation = Station(names, smodules)
