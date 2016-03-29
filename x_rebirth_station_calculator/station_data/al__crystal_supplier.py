from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Crystal Supplier',
         'L049': 'Kristall-Zulieferer'}

smodules = [modules.CrystalCuttery(production_method='al', efficiency=145),
            modules.CrystalCuttery(production_method='al', efficiency=141),
            modules.CrystalCuttery(production_method='al', efficiency=141),
            modules.CubePlant(production_method='al', efficiency=141),
            modules.CubePlant(production_method='al', efficiency=141),
            modules.CubePlant(production_method='al', efficiency=141)]

AL_CrystalSupplier = Station(names, smodules)
