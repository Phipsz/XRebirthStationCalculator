from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'URV Parts Supply',
         'L049': 'URV-Teilezulieferer'}

smodules = [(modules.URVWharf, 1),
            (modules.ChipFab, 1),
            (modules.BioOpticsFac, 1),
            (modules.FusionCoreFac, 1),
            (modules.PlasmaTech, 1),
            (modules.PodkletnovFab, 1),
            (modules.ScannArFacility, 1)]

productions = [Production(wares.AssaultURV, 6.16, 128.0),
               Production(wares.CargolifterURV, 18.48, 128.0),
               Production(wares.ConstructionURV, 9.48, 128.0),
               Production(wares.InterceptorURVMk1, 14.76, 128.0),
               Production(wares.InterceptorURVMk2, 4.32, 128.0),
               Production(wares.IntrepidURVMk1, 11.08, 128.0),
               Production(wares.IntrepidURVMk2, 3.08, 128.0),
               Production(wares.OverrunURVMk1, 8.6, 128.0),
               Production(wares.OverrunURVMk2, 2.48, 128.0),
               Production(wares.ScoopCollectorURVMk1, 16.0, 128.0),
               Production(wares.ScoopCollectorURVMk2, 4.92, 128.0),
               Production(wares.SurfaceMinerURVMk1, 17.24, 128.0),
               Production(wares.SurfaceMinerURVMk2, 4.92, 128.0),
               Production(wares.Microchips, 640.0, 147.0),
               Production(wares.BioOpticWiring, 240.0, 151.0),
               Production(wares.FusionReactors, 120.0, 147.0),
               Production(wares.PlasmaFlowRegulators, 40.0, 148.0),
               Production(wares.PodkletnovGenerators, 72.0, 148.0),
               Production(wares.ScanningArray, 80.0, 150.0)]

consumptions = [Consumption(wares.AntimatterCells, 2760.0),
                Consumption(wares.BioOpticWiring, 125.0),
                Consumption(wares.ChemicalCompounds, 560.0),
                Consumption(wares.CutCrystals, 640.0),
                Consumption(wares.EnergyCells, 6738.0),
                Consumption(wares.FoodRations, 2985.0),
                Consumption(wares.FusionReactors, 6.0),
                Consumption(wares.IonCells, 768.0),
                Consumption(wares.MedicalSupplies, 1608.0, True),
                Consumption(wares.Microchips, 728.0),
                Consumption(wares.NividiumCubes, 1296.0),
                Consumption(wares.PlasmaCells, 800.0),
                Consumption(wares.PlasmaFlowRegulators, 9.0),
                Consumption(wares.PodkletnovGenerators, 8.0),
                Consumption(wares.QuantumTubes, 476.0),
                Consumption(wares.RefinedMetals, 1240.0),
                Consumption(wares.ReinforcedMetalPlating, 16.0),
                Consumption(wares.ScanningArray, 41.0),
                Consumption(wares.SiliconWafers, 3440.0),
                Consumption(wares.Spacefuel, 1272.0, True)]

AL_URVPartsSupply = Station(names, smodules, productions, consumptions)
