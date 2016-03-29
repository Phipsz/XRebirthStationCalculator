from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Ion Cell Plant',
         'L049': 'Ionenzellen-Fertigung'}

productions = {'al': [Production(wares.IonCells, 720)],
               'ar': [Production(wares.IonCells, 960)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 1600),
                       Consumption(wares.FoodRations, 720),
                       Consumption(wares.Ions, 1600),
                       Consumption(wares.Spacefuel, 120, True)],

                'ar': [Consumption(wares.BoFu, 400),
                       Consumption(wares.EnergyCells, 1600),
                       Consumption(wares.Ions, 2400),
                       Consumption(wares.Spacefuel, 160, True)]}

IonCellPlant = Module(names, productions, consumptions)
