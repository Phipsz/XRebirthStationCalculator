from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Integrative URV Forge',
         'L049': 'Integrative URV-Montage'}

smodules = [modules.SteelRefinery(production_method='al', efficiency=157),
            modules.SteelRefinery(production_method='al', efficiency=150),
            modules.WaferPlant(production_method='al', efficiency=144),
            modules.WaferPlant(production_method='al', efficiency=150),
            modules.URVWharf(production_method='dv', efficiency=111),
            modules.URVWharf(production_method='dv', efficiency=109)]

DV_IntegrativeURVForge = Station(names, smodules)
