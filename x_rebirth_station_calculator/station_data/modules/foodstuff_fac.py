from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Foodstuff Fac',
         'L049': 'Nahrungsmittel-Anl'}

productions = {'al': [Production(wares.FoodRations, 12000)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 2400),
                       Consumption(wares.Meat, 1200),
                       Consumption(wares.Spices, 1200),
                       Consumption(wares.Wheat, 4800)]}

FoodstuffFac = Module(names, productions, consumptions)
