from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Fusion Core Fac',
         'L049': 'Fusionskern-Anl'}

productions = {'al': [Production(wares.FusionReactors, 120)],
               'ar': [Production(wares.FusionReactors, 120)]}

consumptions = {'al': [Consumption(wares.AntimatterCells, 1800),
                       Consumption(wares.EnergyCells, 1440),
                       Consumption(wares.FoodRations, 480),
                       Consumption(wares.Microchips, 240),
                       Consumption(wares.NividiumCubes, 720),
                       Consumption(wares.QuantumTubes, 180),
                       Consumption(wares.RefinedMetals, 600),
                       Consumption(wares.MedicalSupplies, 480, True),
                       Consumption(wares.Spacefuel, 420, True)],

                'ar': [Consumption(wares.AntimatterCells, 1800),
                       Consumption(wares.BioElectricNeuronGel, 210),
                       Consumption(wares.BoFu, 300),
                       Consumption(wares.EnergyCells, 960),
                       Consumption(wares.NividiumCubes, 720),
                       Consumption(wares.QuantumTubes, 150),
                       Consumption(wares.RefinedMetals, 720),
                       Consumption(wares.MedicalSupplies, 540, True),
                       Consumption(wares.Spacefuel, 210, True)]}

FusionCoreFac = Module(names, productions, consumptions)
