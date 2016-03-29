from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'URV Wharf',
         'L049': 'URV-Landeplatz'}

productions = {'dv': [Production(wares.CargolifterURV, 4.7),
                      Production(wares.ConstructionURV, 2),
                      Production(wares.InterceptorURVMk1, 2.7),
                      Production(wares.ScoopCollectorURVMk1, 2),
                      Production(wares.SurfaceMinerURVMk1, 2.7)],

               'al': [Production(wares.AssaultURV, 1.5),
                      Production(wares.CargolifterURV, 4.6),
                      Production(wares.ConstructionURV, 2.5),
                      Production(wares.InterceptorURVMk1, 3.7),
                      Production(wares.InterceptorURVMk2, 1.1),
                      Production(wares.IntrepidURVMk1, 2.8),
                      Production(wares.IntrepidURVMk2, 0.8),
                      Production(wares.OverrunURVMk1, 2.2),
                      Production(wares.OverrunURVMk2, 0.6),
                      Production(wares.ScoopCollectorURVMk1, 4),
                      Production(wares.ScoopCollectorURVMk2, 1.2),
                      Production(wares.SurfaceMinerURVMk1, 4.3),
                      Production(wares.SurfaceMinerURVMk2, 1.2)],

               'ar': [Production(wares.AssaultURV, 1.5),
                      Production(wares.CargolifterURV, 4.6),
                      Production(wares.ConstructionURV, 2.5),
                      Production(wares.InterceptorURVMk1, 3.7),
                      Production(wares.InterceptorURVMk2, 1.1),
                      Production(wares.IntrepidURVMk1, 2.8),
                      Production(wares.IntrepidURVMk2, 0.8),
                      Production(wares.OverrunURVMk1, 2.2),
                      Production(wares.OverrunURVMk2, 0.6),
                      Production(wares.ScoopCollectorURVMk1, 4),
                      Production(wares.ScoopCollectorURVMk2, 1.2),
                      Production(wares.SurfaceMinerURVMk1, 4.3),
                      Production(wares.SurfaceMinerURVMk2, 1.2)]}

consumptions = {'dv': [Consumption(wares.Crystals, 946),
                       Consumption(wares.EnergyCells, 195),
                       Consumption(wares.FoodRations, 134),
                       Consumption(wares.Nividium, 884),
                       Consumption(wares.Ore, 1665),
                       Consumption(wares.Silicon, 1481)],

                'al': [Consumption(wares.BioOpticWiring, 125),
                       Consumption(wares.EnergyCells, 386),
                       Consumption(wares.FoodRations, 265),
                       Consumption(wares.FusionReactors, 6),
                       Consumption(wares.PodkletnovGenerators, 8),
                       Consumption(wares.Microchips, 24),
                       Consumption(wares.PlasmaFlowRegulators, 9),
                       Consumption(wares.ReinforcedMetalPlating, 16),
                       Consumption(wares.ScanningArray, 41)],

                'ar': [Consumption(wares.BioElectricNeuronGel, 99),
                       Consumption(wares.BoFu, 133),
                       Consumption(wares.EMSpectrometer, 45),
                       Consumption(wares.EnergyCells, 383),
                       Consumption(wares.FusionReactors, 6),
                       Consumption(wares.PodkletnovGenerators, 8),
                       Consumption(wares.PlasmaFlowRegulators, 9),
                       Consumption(wares.PlasmaPumps, 75),
                       Consumption(wares.ReinforcedMetalPlating, 16)]}

URVWharf = Module(names, productions, consumptions)
