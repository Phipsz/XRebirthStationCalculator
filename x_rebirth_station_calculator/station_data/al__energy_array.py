from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Energy Array',
         'L049': 'Energiematrix'}

smodules = [modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142),
            modules.ECellFab(production_method='al', efficiency=142)]

AL_EnergyArray = Station(names, smodules)
