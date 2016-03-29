from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Water Distillery',
         'L049': 'Wasserveredelung'}

smodules = [modules.CondenserStill(production_method='al', efficiency=143.0),
            modules.CondenserStill(production_method='al', efficiency=143.0)]

DV_WaterDistillery = Station(names, smodules)
