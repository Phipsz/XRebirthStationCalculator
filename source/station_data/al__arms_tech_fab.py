from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Arms Tech Fab',
         'L049': 'Waffen-Tech Fab'}

smodules = [(modules.PlateFoundry, 1),
            (modules.ScannArFacility, 1),
            (modules.WarheadForge, 1),
            (modules.MissileForge, 1),
            (modules.TurretForge, 1),
            (modules.ShieldFacility, 1)]

productions = [Production(wares.ReinforcedMetalPlating, 400.0, 165.0),
               Production(wares.ScanningArray, 80.0, 151.0),
               Production(wares.WarheadComponents, 40.0, 147.0),
               Production(wares.NewtonianVCrushers, 169.0, 147.0),
               Production(wares.Novadrones, 11.0, 147.0),
               Production(wares.SunstalkerMissiles, 57.0, 147.0),
               Production(wares.AstrobeeSwarmkillers, 29.0, 147.0),
               Production(wares.HITMATurret, 32.0, 134.0),
               Production(wares.PlasmaMATurret, 24.0, 134.0),
               Production(wares.VLauncher, 8.0, 134.0),
               Production(wares.HailstormMATurret, 24.0, 134.0),
               Production(wares.PlasmaJETLRTurret, 12.0, 134.0),
               Production(wares.AstrobeeLauncher, 4.0, 134.0),
               Production(wares.ForceFieldProjector, 80.0, 131.0)]

consumptions = [Consumption(wares.AntimatterCells, 480.0),
                Consumption(wares.BioOpticWiring, 602.0),
                Consumption(wares.ChemicalCompounds, 600.0),
                Consumption(wares.CutCrystals, 640.0),
                Consumption(wares.EnergyCells, 3688.0),
                Consumption(wares.FoodRations, 2040.0),
                Consumption(wares.FusionReactors, 140.0),
                Consumption(wares.MedicalSupplies, 591.43, True),
                Consumption(wares.Microchips, 146.0),
                Consumption(wares.NividiumCubes, 640.0),
                Consumption(wares.Narcotics, 274.29, True),
                Consumption(wares.PlasmaCells, 160.0),
                Consumption(wares.QuantumTubes, 71.0),
                Consumption(wares.ReinforcedMetalPlating, 592.0),
                Consumption(wares.RefinedMetals, 2880.0),
                Consumption(wares.ScanningArray, 9.0),
                Consumption(wares.Spacefuel, 1800.0, True),
                Consumption(wares.SiliconWafers, 400.0),
                Consumption(wares.WarheadComponents, 31.0)]

AL_ArmsTechFab = Station(names, smodules, productions, consumptions)
