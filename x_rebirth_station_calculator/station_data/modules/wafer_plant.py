from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Wafer Plant',
         'L049': 'Siliziumscheibenfabrik'}

productions = {'al': [Production(wares.SiliconWafers, 1320)],
               'ar': [Production(wares.SiliconWafers, 1320)]}

consumptions = {'al': [Consumption(wares.CutCrystals, 240),
                       Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.FoodRations, 1440),
                       Consumption(wares.Silicon, 2400),
                       Consumption(wares.MedicalSupplies, 12, True),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 12, True)],

                'ar': [Consumption(wares.BoFu, 660),
                       Consumption(wares.CutCrystals, 240),
                       Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.Silicon, 2400),
                       Consumption(wares.Narcotics, 120, True),
                       Consumption(wares.Spacefuel, 12, True)]}

WaferPlant = Module(names, productions, consumptions)
