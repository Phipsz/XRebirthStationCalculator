from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Ice Refinery',
         'L049': 'Eis-Raffinerie'}

productions = {'universal': [Production(wares.Ice, 3000)]}

consumptions = {'universal': [Consumption(wares.EnergyCells, 2400)]}

IceRefinery = Module(names, productions, consumptions)
