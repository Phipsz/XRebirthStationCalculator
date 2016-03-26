from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Wheat Plantation',
         'L049': 'Weizenplantage'}

smodules = [(modules.ValleyForge, 2)]

productions = [Production(wares.Wheat, 10800.0, 100.0)]

consumptions = [Consumption(wares.Water, 6000.0),
                Consumption(wares.EnergyCells, 4800.0)]

DV_WheatPlantation = Station(names, smodules, productions, consumptions)
