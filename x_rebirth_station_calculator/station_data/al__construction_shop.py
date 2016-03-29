from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Construction Shop',
         'L049': 'Baumarkt'}

smodules = [modules.PlateFoundry(production_method='al', efficiency=157),
            modules.PlateFoundry(production_method='al', efficiency=137),
            modules.PlateFoundry(production_method='al', efficiency=144),
            modules.SteelRefinery(production_method='al', efficiency=146),
            modules.SteelRefinery(production_method='al', efficiency=140),
            modules.SteelRefinery(production_method='al', efficiency=146),
            modules.ChemRefinery(production_method='al', efficiency=144),
            modules.ChemRefinery(production_method='al', efficiency=142)]

AL_ConstructionShop = Station(names, smodules)
