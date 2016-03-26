from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Mega Cellfab',
         'L049': 'Mega-Zell-Fab'}

smodules = [(modules.PlasmaCyclotron, 3),
            (modules.IonCellPlant, 3),
            (modules.AMCyclotron, 3)]

productions = [Production(wares.PlasmaCells, 2880.0, 157.0),
               Production(wares.IonCells, 2880.0, 151.33),
               Production(wares.AntimatterCells, 2880.0, 145.0)]

consumptions = [Consumption(wares.EnergyCells, 16800.0),
                Consumption(wares.BoFu, 3600.0),
                Consumption(wares.Plasma, 7200.0),
                Consumption(wares.Ions, 7200.0),
                Consumption(wares.Hydrogen, 10800.0),
                Consumption(wares.Spacefuel, 1440.0, True)]

OL_MegaCellfab = Station(names, smodules, productions, consumptions)
