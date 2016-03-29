from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Narcotics Lab',
         'L049': 'Narkotika Labor'}

productions = {'universal': [Production(wares.Narcotics, 1440)]}

consumptions = {'universal': [Consumption(wares.EnergyCells, 720),
                              Consumption(wares.Spaceweed, 1200)]}

NarcoticsLab = Module(names, productions, consumptions)
