from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'URV Integration',
         'L049': 'URV-Endfertigungsanlage'}

smodules = [modules.URVWharf(production_method='ar', efficiency=147),
            modules.URVWharf(production_method='ar', efficiency=124),
            modules.FusionCoreFac(production_method='ar', efficiency=166),
            modules.PodkletnovFab(production_method='ar', efficiency=166),
            modules.PlasmaTech(production_method='ar', efficiency=166),
            modules.PlateFoundry(production_method='ar', efficiency=170)]

OL_URVIntegration = Station(names, smodules)
