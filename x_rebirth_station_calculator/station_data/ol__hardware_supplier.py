from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Hardware Supplier',
         'L049': 'Material-Zulieferer'}

smodules = [modules.PlateFoundry(production_method='ar', efficiency=160),
            modules.PlateFoundry(production_method='ar', efficiency=160),
            modules.SteelRefinery(production_method='ar', efficiency=158),
            modules.SteelRefinery(production_method='ar', efficiency=160),
            modules.SteelRefinery(production_method='ar', efficiency=161),
            modules.ChemRefinery(production_method='ar', efficiency=157),
            modules.ChemRefinery(production_method='ar', efficiency=157)]

OL_HardwareSupplier = Station(names, smodules)
