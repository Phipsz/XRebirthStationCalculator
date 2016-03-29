from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Plankton Tankfarm',
         'L049': 'Plankton-Tankfarm'}

smodules = [modules.PlanktonTank(production_method='ar', efficiency=196),
            modules.PlanktonTank(production_method='ar', efficiency=196),
            modules.PlanktonTank(production_method='ar', efficiency=186),
            modules.PlanktonTank(production_method='ar', efficiency=186),
            modules.PlanktonTank(production_method='ar', efficiency=183),
            modules.PlanktonTank(production_method='ar', efficiency=183),
            modules.PlanktonTank(production_method='ar', efficiency=183),
            modules.PlanktonTank(production_method='ar', efficiency=183),
            modules.PlanktonTank(production_method='ar', efficiency=186),
            modules.PlanktonTank(production_method='ar', efficiency=186),
            modules.PlanktonTank(production_method='ar', efficiency=183),
            modules.PlanktonTank(production_method='ar', efficiency=183)]

OL_PlanktonTankfarm = Station(names, smodules)
