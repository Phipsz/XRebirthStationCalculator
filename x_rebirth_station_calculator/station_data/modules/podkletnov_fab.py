from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Podkletnov Fab',
         'L049': 'Podkletnov-Fab'}

productions = {'al': [Production(wares.PodkletnovGenerators, 72)],
               'ar': [Production(wares.PodkletnovGenerators, 72)]}

consumptions = {'al': [Consumption(wares.AntimatterCells, 960),
                       Consumption(wares.EnergyCells, 1152),
                       Consumption(wares.FoodRations, 480),
                       Consumption(wares.IonCells, 768),
                       Consumption(wares.Microchips, 144),
                       Consumption(wares.NividiumCubes, 576),
                       Consumption(wares.QuantumTubes, 96),
                       Consumption(wares.SiliconWafers, 1440),
                       Consumption(wares.MedicalSupplies, 408, True),
                       Consumption(wares.Spacefuel, 312, True)],

                'ar': [Consumption(wares.AntimatterCells, 936),
                       Consumption(wares.BioElectricNeuronGel, 96),
                       Consumption(wares.BoFu, 312),
                       Consumption(wares.EnergyCells, 1200),
                       Consumption(wares.IonCells, 768),
                       Consumption(wares.NividiumCubes, 672),
                       Consumption(wares.QuantumTubes, 96),
                       Consumption(wares.SiliconWafers, 1488),
                       Consumption(wares.MedicalSupplies, 456, True),
                       Consumption(wares.Spacefuel, 144, True)]}

PodkletnovFab = Module(names, productions, consumptions)
