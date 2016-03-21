from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Metalframes Fab',
         'L049': 'Metallschmiede'}

smodules = [(modules.SteelRefinery, 4),
            (modules.WaferPlant, 4)]

productions = [Production(wares.RefinedMetals, 4800.0, 147.0),
               Production(wares.SiliconWafers, 5280.0, 145.5)]

consumptions = [Consumption(wares.CutCrystals, 960.0),
                Consumption(wares.EnergyCells, 16320.0),
                Consumption(wares.BoFu, 5280.0),
                Consumption(wares.Narcotics, 960.0, True),
                Consumption(wares.Ore, 9600.0),
                Consumption(wares.Silicon, 9600.0),
                Consumption(wares.Spacefuel, 96.0, True)]

OL_MetalframesFab = Station(names, smodules, productions, consumptions)
