from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Pharma Lab',
         'L049': 'Pharma-Lab'}

smodules = [modules.NarcoticsLab(efficiency=156),
            modules.NarcoticsLab(efficiency=154),
            modules.NarcoticsLab(efficiency=150),
            modules.NarcoticsLab(efficiency=150),
            modules.PharmaPlatform(efficiency=156),
            modules.PharmaPlatform(efficiency=151),
            modules.PharmaPlatform(efficiency=151),
            modules.PharmaPlatform(efficiency=156),
            modules.HerbGarden(efficiency=158),
            modules.HerbGarden(efficiency=152),
            modules.HerbGarden(efficiency=152),
            modules.HerbGarden(efficiency=156)]

OL_PharmaLab = Station(names, smodules)
