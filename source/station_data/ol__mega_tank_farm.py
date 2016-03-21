from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Mega-Tank Farm',
         'L049': 'Megaaquarium-Farm'}

smodules = [(modules.SpiceTubes, 2),
            (modules.PlanktonTank, 2),
            (modules.SoyBeanery, 2)]

productions = [Production(wares.Spices, 6400.0, 156.0),
               Production(wares.Plankton, 11520.0, 157.0),
               Production(wares.SoyBeans, 5760.0, 170.0)]

consumptions = [Consumption(wares.EnergyCells, 5440.0),
                Consumption(wares.Water, 18720.0)]

OL_MegaTankFarm = Station(names, smodules, productions, consumptions)
