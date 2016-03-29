from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'QTube Y Fab',
         'L049': 'Quantumröhren-Y-Fab'}

productions = {'al': [Production(wares.QuantumTubes, 240)],
               'ar': [Production(wares.QuantumTubes, 240)]}

consumptions = {'al': [Consumption(wares.ChemicalCompounds, 300),
                       Consumption(wares.EnergyCells, 1200),
                       Consumption(wares.FoodRations, 480),
                       Consumption(wares.NividiumCubes, 360),
                       Consumption(wares.RefinedMetals, 720),
                       Consumption(wares.MedicalSupplies, 120, True),
                       Consumption(wares.Spacefuel, 150, True)],

                'ar': [Consumption(wares.BoFu, 270),
                       Consumption(wares.ChemicalCompounds, 240),
                       Consumption(wares.EnergyCells, 1200),
                       Consumption(wares.NividiumCubes, 360),
                       Consumption(wares.RefinedMetals, 900),
                       Consumption(wares.MedicalSupplies, 120, True),
                       Consumption(wares.Spacefuel, 60, True)]}

QTubeYFab = Module(names, productions, consumptions)
