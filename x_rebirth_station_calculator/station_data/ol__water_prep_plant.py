from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Water Prep Plant',
         'L049': 'Wasseraufbereitungsanlage'}

smodules = [(modules.CondenserStill, 4)]

productions = [Production(wares.Water, 48000.0, 144.0)]

consumptions = [Consumption(wares.Ice, 38400.0),
                Consumption(wares.EnergyCells, 9600.0)]

OL_WaterPrepPlant = Station(names, smodules, productions, consumptions)