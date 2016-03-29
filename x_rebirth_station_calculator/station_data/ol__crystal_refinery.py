from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Crystal Refinery',
         'L049': 'Kristall-Raffinerie'}

smodules = [modules.CrystalCuttery(production_method='ar', efficiency=169),
            modules.CrystalCuttery(production_method='ar', efficiency=164),
            modules.CrystalCuttery(production_method='ar', efficiency=158),
            modules.CubePlant(production_method='ar', efficiency=162),
            modules.CubePlant(production_method='ar', efficiency=160),
            modules.CubePlant(production_method='ar', efficiency=158)]

OL_CrystalRefinery = Station(names, smodules)
