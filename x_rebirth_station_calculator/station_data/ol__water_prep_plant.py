from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Water Prep Plant',
         'L049': 'Wasseraufbereitungsanlage'}

smodules = [modules.CondenserStill(production_method='ar', efficiency=143),
            modules.CondenserStill(production_method='ar', efficiency=143),
            modules.CondenserStill(production_method='ar', efficiency=143),
            modules.CondenserStill(production_method='ar', efficiency=143)]

OL_WaterPrepPlant = Station(names, smodules)
