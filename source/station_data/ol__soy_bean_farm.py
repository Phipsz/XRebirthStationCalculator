from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Soy Bean Farm',
         'L049': 'Sojabohnenplantage'}

smodules = [(modules.SoyBeanery, 6)]

productions = [Production(wares.Plankton, 17280.0, 182.0)]

consumptions = [Consumption(wares.EnergyCells, 8640.0),
                Consumption(wares.Water, 17280.0)]

OL_SoyBeanFarm = Station(names, smodules, productions, consumptions)
