from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Turret Forge',
         'L049': 'Geschützturmschmiede'}

productions = {'al': [Production(wares.AstrobeeLauncher, 4),
                      Production(wares.HailstormMATurret, 24),
                      Production(wares.HITMATurret, 32),
                      Production(wares.PlasmaJETLRTurret, 12),
                      Production(wares.PlasmaMATurret, 24),
                      Production(wares.VLauncher, 8)],

               'ar': [Production(wares.AstrobeeLauncher, 4),
                      Production(wares.HailstormMATurret, 24),
                      Production(wares.HITMATurret, 32),
                      Production(wares.PlasmaJETLRTurret, 12),
                      Production(wares.PlasmaMATurret, 24),
                      Production(wares.VLauncher, 8)]}

consumptions = {'al': [Consumption(wares.BioOpticWiring, 588),
                       Consumption(wares.EnergyCells, 808),
                       Consumption(wares.FusionReactors, 140),
                       Consumption(wares.ReinforcedMetalPlating, 592)],

                'ar': [Consumption(wares.EnergyCells, 808),
                       Consumption(wares.FusionReactors, 140),
                       Consumption(wares.PlasmaPumps, 441),
                       Consumption(wares.ReinforcedMetalPlating, 592)]}

TurretForge = Module(names, productions, consumptions)
