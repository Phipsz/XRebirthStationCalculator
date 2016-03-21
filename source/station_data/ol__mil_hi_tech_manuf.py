from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Mil Hi-Tech Manuf',
         'L049': 'Mil Hi-Tech Manuf'}

smodules = [(modules.MissileForge, 2),
            (modules.TurretForge, 2),
            (modules.ShieldFacility, 2)]

productions = [Production(wares.NewtonianVCrushers, 338.0, 153.0),
               Production(wares.Novadrones, 23.0, 153.0),
               Production(wares.SunstalkerMissiles, 114.0, 153.0),
               Production(wares.AstrobeeSwarmkillers, 57.0, 153.0),
               Production(wares.HITMATurret, 64.0, 135.0),
               Production(wares.PlasmaMATurret, 48.0, 135.0),
               Production(wares.VLauncher, 16.0, 135.0),
               Production(wares.HailstormMATurret, 48.0, 135.0),
               Production(wares.PlasmaJETLRTurret, 24.0, 135.0),
               Production(wares.AstrobeeLauncher, 8.0, 135.0),
               Production(wares.ForceFieldProjector, 160.0, 134.0)]

consumptions = [Consumption(wares.BioElectricNeuronGel, 51.0),
                Consumption(wares.BoFu, 303.0),
                Consumption(wares.EMSpectrometer, 17.0),
                Consumption(wares.EnergyCells, 3536.0),
                Consumption(wares.FusionReactors, 360.0),
                Consumption(wares.MedicalSupplies, 377.14, True),
                Consumption(wares.Narcotics, 582.86, True),
                Consumption(wares.PlasmaPumps, 1391.0),
                Consumption(wares.QuantumTubes, 23.0),
                Consumption(wares.ReinforcedMetalPlating, 1504.0),
                Consumption(wares.WarheadComponents, 63.0)]

OL_MilHiTechManuf = Station(names, smodules, productions, consumptions)
