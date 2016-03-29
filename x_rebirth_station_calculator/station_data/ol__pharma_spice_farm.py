from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Pharma-Spice Farm',
         'L049': 'Heilpflanzenplantage'}

smodules = [modules.SpiceTubes(efficiency=166),
            modules.SpiceTubes(efficiency=163),
            modules.SpiceTubes(efficiency=163),
            modules.HerbGarden(efficiency=167),
            modules.HerbGarden(efficiency=167),
            modules.HerbGarden(efficiency=167)]

OL_PharmaSpiceFarm = Station(names, smodules)
