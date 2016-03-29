from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Cell Recharge Fac (OL)',
         'L049': 'Zellenladeanlage (OL)'}

smodules = [modules.FuelCellMill(production_method='ar', efficiency=193),
            modules.FuelCellMill(production_method='ar', efficiency=193),
            modules.FuelCellMill(production_method='ar', efficiency=193),
            modules.FuelCellMill(production_method='ar', efficiency=193)]

OL_CellRechargeFac = Station(names, smodules)
