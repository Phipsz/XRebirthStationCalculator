from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Cell Recharge Fac (AL)',
         'L049': 'Zellenladeanlage (AL)'}

smodules = [modules.FuelCellMill(production_method='al', efficiency=193),
            modules.FuelCellMill(production_method='al', efficiency=193),
            modules.FuelCellMill(production_method='al', efficiency=193),
            modules.FuelCellMill(production_method='al', efficiency=193)]

AL_CellRechargeFac = Station(names, smodules)
