from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'ScannAr Facility',
         'L049': 'ScannAr-Fabrik'}

productions = {'al': [Production(wares.ScanningArray, 80)]}

consumptions = {'al': [Consumption(wares.ChemicalCompounds, 80),
                       Consumption(wares.CutCrystals, 640),
                       Consumption(wares.EnergyCells, 640),
                       Consumption(wares.FoodRations, 400),
                       Consumption(wares.Microchips, 80),
                       Consumption(wares.QuantumTubes, 40),
                       Consumption(wares.RefinedMetals, 320),
                       Consumption(wares.SiliconWafers, 400),
                       Consumption(wares.MedicalSupplies, 160, True),
                       Consumption(wares.Spacefuel, 120, True)]}

ScannArFacility = Module(names, productions, consumptions)
