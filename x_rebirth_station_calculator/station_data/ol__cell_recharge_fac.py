from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Cell Recharge Fac (OL)',
         'L049': 'Zellenladeanlage (OL)'}

smodules = [(modules.FuelCellMill, 1)]

productions = [Production(wares.FuelCells, 21600.0, 178.0)]

consumptions = [Consumption(wares.EnergyCells, 19200.0),
                Consumption(wares.BoFu, 1200.0),
                Consumption(wares.Spacefuel, 480.0, True)]

OL_CellRechargeFac = Station(names, smodules, productions, consumptions)