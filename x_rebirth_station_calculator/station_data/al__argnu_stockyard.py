from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Argnu Stockyard',
         'L049': 'Argnu-Zuchtplantagen'}

smodules = [(modules.ArgnuParadise, 4)]

productions = [Production(wares.Meat, 7680.0, 100.0)]

consumptions = [Consumption(wares.Water, 6720.0),
                Consumption(wares.Wheat, 6720.0),
                Consumption(wares.EnergyCells, 2880.0)]

AL_ArgnuStockyard = Station(names, smodules, productions, consumptions)