from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'A/M Cyclotron',
         'L049': 'A/M-Zyklotron'}

productions = {'al': [Production(wares.AntimatterCells, 800)],
               'ar': [Production(wares.AntimatterCells, 960)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 1600),
                       Consumption(wares.FoodRations, 720),
                       Consumption(wares.Hydrogen, 3200),
                       Consumption(wares.Spacefuel, 120, True)],

                'ar': [Consumption(wares.BoFu, 400),
                       Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.Hydrogen, 3600),
                       Consumption(wares.Spacefuel, 160, True)]}

AMCyclotron = Module(names, productions, consumptions)
