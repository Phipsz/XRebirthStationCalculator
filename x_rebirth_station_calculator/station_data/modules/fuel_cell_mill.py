from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Fuel Cell Mill',
         'L049': 'Sprungzellenproduktion'}

productions = {'al': [Production(wares.FuelCells, 5400)],
               'ar': [Production(wares.FuelCells, 5400)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 4800),
                       Consumption(wares.FoodRations, 720),
                       Consumption(wares.Spacefuel, 120, True)],

                'ar': [Consumption(wares.EnergyCells, 4800),
                       Consumption(wares.BoFu, 300),
                       Consumption(wares.Spacefuel, 120, True)]}

FuelCellMill = Module(names, productions, consumptions)
