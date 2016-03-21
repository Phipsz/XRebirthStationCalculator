from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Cell Recharge Fac (AL)',
         'L049': 'Zellenladeanlage (AL)'}

smodules = [(modules.FuelCellMill, 1)]

productions = [Production(wares.FuelCells, 21600.0, 178.0)]

consumptions = [Consumption(wares.EnergyCells, 19200.0),
                Consumption(wares.FoodRations, 2880.0),
                Consumption(wares.Spacefuel, 480.0, True)]

AL_CellRechargeFac = Station(names, smodules, productions, consumptions)
