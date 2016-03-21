from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Arms Tech Supply',
         'L049': 'Waffen-Tech Zulieferer'}

smodules = [(modules.MissileForge, 2),
            (modules.TurretForge, 2),
            (modules.ShieldFacility, 2)]

productions = [Production(wares.NewtonianVCrushers, 338.0, 147.0),
               Production(wares.Novadrones, 23.0, 147.0),
               Production(wares.SunstalkerMissiles, 114.0, 147.0),
               Production(wares.AstrobeeSwarmkillers, 57.0, 147.0),
               Production(wares.HITMATurret, 64.0, 134.0),
               Production(wares.PlasmaMATurret, 48.0, 134.0),
               Production(wares.VLauncher, 16.0, 134.0),
               Production(wares.HailstormMATurret, 48.0, 134.0),
               Production(wares.PlasmaJETLRTurret, 24.0, 134.0),
               Production(wares.AstrobeeLauncher, 8.0, 134.0),
               Production(wares.ForceFieldProjector, 160.0, 131.0)]

consumptions = [Consumption(wares.BioOpticWiring, 1844.0),
                Consumption(wares.EnergyCells, 3536.0),
                Consumption(wares.FoodRations, 720.0),
                Consumption(wares.FusionReactors, 360.0),
                Consumption(wares.MedicalSupplies, 342.86, True),
                Consumption(wares.Microchips, 52.0),
                Consumption(wares.Narcotics, 548.58, True),
                Consumption(wares.QuantumTubes, 22.0),
                Consumption(wares.ReinforcedMetalPlating, 1504.0),
                Consumption(wares.ScanningArray, 18.0),
                Consumption(wares.WarheadComponents, 62.0)]

AL_ArmsTechSupply = Station(names, smodules, productions, consumptions)
