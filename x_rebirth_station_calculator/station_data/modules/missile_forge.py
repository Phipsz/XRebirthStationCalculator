from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Missile Forge',
         'L049': 'Raketenschmiede'}

productions = {'al': [Production(wares.AstrobeeSwarmkillers, 28.6),
                      Production(wares.NewtonianVCrushers, 169.1),
                      Production(wares.Novadrones, 11.4),
                      Production(wares.SunstalkerMissiles, 57.1)],

               'ar': [Production(wares.AstrobeeSwarmkillers, 28.6),
                      Production(wares.NewtonianVCrushers, 169.1),
                      Production(wares.Novadrones, 11.4),
                      Production(wares.SunstalkerMissiles, 57.1)]}

consumptions = {'al': [Consumption(wares.BioOpticWiring, 14),
                       Consumption(wares.EnergyCells, 480),
                       Consumption(wares.FoodRations, 360),
                       Consumption(wares.Microchips, 26),
                       Consumption(wares.QuantumTubes, 11),
                       Consumption(wares.ScanningArray, 9),
                       Consumption(wares.WarheadComponents, 31),
                       Consumption(wares.MedicalSupplies, 171, True),
                       Consumption(wares.Narcotics, 274, True)],

                'ar': [Consumption(wares.BioElectricNeuronGel, 26),
                       Consumption(wares.BoFu, 151),
                       Consumption(wares.EMSpectrometer, 9),
                       Consumption(wares.EnergyCells, 480),
                       Consumption(wares.PlasmaPumps, 14),
                       Consumption(wares.QuantumTubes, 11),
                       Consumption(wares.WarheadComponents, 31),
                       Consumption(wares.MedicalSupplies, 189, True),
                       Consumption(wares.Narcotics, 291, True)]}

MissileForge = Module(names, productions, consumptions)
