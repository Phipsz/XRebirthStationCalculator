from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'URV Integration',
         'L049': 'URV-Endfertigungsanlage'}

smodules = [(modules.URVWharf, 2),
            (modules.FusionCoreFac, 1),
            (modules.PodkletnovFab, 1),
            (modules.PlasmaTech, 1),
            (modules.PlateFoundry, 1)]

productions = [Production(wares.AssaultURV, 3.08, 135.5),
               Production(wares.CargolifterURV, 9.24, 135.5),
               Production(wares.ConstructionURV, 4.92, 135.5),
               Production(wares.InterceptorURVMk1, 7.38, 135.5),
               Production(wares.InterceptorURVMk2, 2.16, 135.5),
               Production(wares.IntrepidURVMk1, 5.54, 135.5),
               Production(wares.IntrepidURVMk2, 1.54, 135.5),
               Production(wares.OverrunURVMk1, 4.3, 135.5),
               Production(wares.OverrunURVMk2, 1.24, 135.5),
               Production(wares.ScoopCollectorURVMk1, 8.0, 135.5),
               Production(wares.ScoopCollectorURVMk2, 2.46, 135.5),
               Production(wares.SurfaceMinerURVMk1, 8.62, 135.5),
               Production(wares.SurfaceMinerURVMk2, 2.46, 135.5),
               Production(wares.FusionReactors, 120.0, 158.0),
               Production(wares.PodkletnovGenerators, 72.0, 158.0),
               Production(wares.PlasmaFlowRegulators, 40.0, 158.0),
               Production(wares.ReinforcedMetalPlating, 360.0, 161.0)]

consumptions = [Consumption(wares.AntimatterCells, 2736.0),
                Consumption(wares.BioElectricNeuronGel, 684.0),
                Consumption(wares.BoFu, 1658.0),
                Consumption(wares.ChemicalCompounds, 240.0),
                Consumption(wares.EMSpectrometer, 89.0),
                Consumption(wares.EnergyCells, 6927.0),
                Consumption(wares.FusionReactors, 11.0),
                Consumption(wares.IonCells, 768.0),
                Consumption(wares.MedicalSupplies, 1156.0, True),
                Consumption(wares.Narcotics, 380.0, True),
                Consumption(wares.NividiumCubes, 2032.0),
                Consumption(wares.PodkletnovGenerators, 17.0),
                Consumption(wares.PlasmaFlowRegulators, 18.0),
                Consumption(wares.PlasmaPumps, 150.0),
                Consumption(wares.QuantumTubes, 426.0),
                Consumption(wares.RefinedMetals, 2680.0),
                Consumption(wares.ReinforcedMetalPlating, 31.0),
                Consumption(wares.SiliconWafers, 1488.0),
                Consumption(wares.Spacefuel, 1714.0, True)]

OL_URVIntegration = Station(names, smodules, productions, consumptions)
