from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Metalframes Fab',
         'L049': 'Metallschmiede'}

smodules = [modules.SteelRefinery(production_method='ar', efficiency=148),
            modules.SteelRefinery(production_method='ar', efficiency=156),
            modules.SteelRefinery(production_method='ar', efficiency=156),
            modules.SteelRefinery(production_method='ar', efficiency=148),
            modules.WaferPlant(production_method='ar', efficiency=156),
            modules.WaferPlant(production_method='ar', efficiency=148),
            modules.WaferPlant(production_method='ar', efficiency=148),
            modules.WaferPlant(production_method='ar', efficiency=148)]

OL_MetalframesFab = Station(names, smodules)
