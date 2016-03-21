from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Mil Hi-Tech Dept',
         'L049': 'Mil Hi-Tech Abt'}

smodules = [(modules.PlateFoundry, 1),
            (modules.EMFacTower, 1),
            (modules.WarheadForge, 1),
            (modules.MissileForge, 1),
            (modules.TurretForge, 1),
            (modules.ShieldFacility, 1)]

productions = [Production(wares.ReinforcedMetalPlating, 360.0, 154.0),
               Production(wares.EMSpectrometer, 120.0, 147.0),
               Production(wares.WarheadComponents, 40.0, 145.0),
               Production(wares.NewtonianVCrushers, 169.0, 147.0),
               Production(wares.Novadrones, 11.0, 147.0),
               Production(wares.SunstalkerMissiles, 57.0, 147.0),
               Production(wares.AstrobeeSwarmkillers, 29.0, 147.0),
               Production(wares.HITMATurret, 32.0, 133.0),
               Production(wares.PlasmaMATurret, 24.0, 133.0),
               Production(wares.VLauncher, 8.0, 133.0),
               Production(wares.HailstormMATurret, 24.0, 133.0),
               Production(wares.PlasmaJETLRTurret, 12.0, 133.0),
               Production(wares.AstrobeeLauncher, 4.0, 133.0),
               Production(wares.ForceFieldProjector, 80.0, 135.0)]

consumptions = [Consumption(wares.AntimatterCells, 440.0),
                Consumption(wares.BioElectricNeuronGel, 146.0),
                Consumption(wares.BoFu, 911.0),
                Consumption(wares.ChemicalCompounds, 360.0),
                Consumption(wares.CutCrystals, 640.0),
                Consumption(wares.EMSpectrometer, 29.0),
                Consumption(wares.EnergyCells, 5568.0),
                Consumption(wares.FusionReactors, 180.0),
                Consumption(wares.MedicalSupplies, 688.57, True),
                Consumption(wares.Narcotics, 291.43, True),
                Consumption(wares.NividiumCubes, 640.0),
                Consumption(wares.PlasmaPumps, 695.0),
                Consumption(wares.QuantumTubes, 51.0),
                Consumption(wares.RefinedMetals, 2500.0),
                Consumption(wares.ReinforcedMetalPlating, 752.0),
                Consumption(wares.SiliconWafers, 960.0),
                Consumption(wares.Spacefuel, 1380.0, True),
                Consumption(wares.WarheadComponents, 31.0)]

OL_MilHiTechDept = Station(names, smodules, productions, consumptions)
