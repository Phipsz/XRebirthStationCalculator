from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Chip Fab',
         'L049': 'Chip-Fab'}

productions = {'al': [Production(wares.Microchips, 640)]}

consumptions = {'al': [Consumption(wares.ChemicalCompounds, 160),
                       Consumption(wares.EnergyCells, 960),
                       Consumption(wares.FoodRations, 480),
                       Consumption(wares.RefinedMetals, 320),
                       Consumption(wares.SiliconWafers, 1600),
                       Consumption(wares.MedicalSupplies, 160, True),
                       Consumption(wares.Spacefuel, 120, True)]}

ChipFab = Module(names, productions, consumptions)
