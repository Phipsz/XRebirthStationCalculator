from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Steel Refinery',
         'L049': 'Stahl-Raffinerie'}

productions = {'al': [Production(wares.RefinedMetals, 1200)],
               'ar': [Production(wares.RefinedMetals, 1200)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.FoodRations, 1440),
                       Consumption(wares.Ore, 2400),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 12, True)],

                'ar': [Consumption(wares.BoFu, 660),
                       Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.Ore, 2400),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 12, True)]}

SteelRefinery = Module(names, productions, consumptions)
