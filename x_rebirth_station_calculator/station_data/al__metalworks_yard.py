from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Metalworks Yard',
         'L049': 'Metallgießerei'}

smodules = [modules.SteelRefinery(production_method='al', efficiency=152),
            modules.SteelRefinery(production_method='al', efficiency=144),
            modules.SteelRefinery(production_method='al', efficiency=144),
            modules.WaferPlant(production_method='al', efficiency=149),
            modules.WaferPlant(production_method='al', efficiency=141),
            modules.WaferPlant(production_method='al', efficiency=141)]

AL_MetalworksYard = Station(names, smodules)
