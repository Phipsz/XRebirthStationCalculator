from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'H2O Additives Fac',
         'L049': 'H2O Anreicherungs-Anl'}

smodules = [modules.CondenserStill(production_method='al', efficiency=146),
            modules.CondenserStill(production_method='al', efficiency=142),
            modules.CondenserStill(production_method='al', efficiency=142),
            modules.CondenserStill(production_method='al', efficiency=146),
            modules.IceRefinery(efficiency=117),
            modules.IceRefinery(efficiency=117),
            modules.IceRefinery(efficiency=117),
            modules.IceRefinery(efficiency=117)]

AL_H2OAdditivesFac = Station(names, smodules)
