from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Cell Fab Matrix',
         'L049': 'Zell-Fab-Matrix'}

smodules = [(modules.PlasmaCyclotron, 2),
            (modules.IonCellPlant, 2),
            (modules.AMCyclotron, 2)]

productions = [Production(wares.PlasmaCells, 1440.0, 143.0),
               Production(wares.IonCells, 1440.0, 139.0),
               Production(wares.AntimatterCells, 1600.0, 139.0)]

consumptions = [Consumption(wares.EnergyCells, 9600.0),
                Consumption(wares.FoodRations, 4320.0),
                Consumption(wares.Plasma, 3200.0),
                Consumption(wares.Ions, 3200.0),
                Consumption(wares.Hydrogen, 6400.0),
                Consumption(wares.Spacefuel, 720.0, True)]

AL_CellFabMatrix = Station(names, smodules, productions, consumptions)
