from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Herb Garden',
         'L049': 'Kräutergarten'}

productions = {'universal': [Production(wares.Spaceweed, 1200)]}

consumptions = {'universal': [Consumption(wares.EnergyCells, 480),
                              Consumption(wares.Spacefuel, 240),
                              Consumption(wares.Water, 1200)]}

HerbGarden = Module(names, productions, consumptions)
