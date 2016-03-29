from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Shield Facility',
         'L049': 'Schildfabrik'}

productions = {'al': [Production(wares.ForceFieldProjector, 80)],
               'ar': [Production(wares.ForceFieldProjector, 80)]}

consumptions = {'al': [Consumption(wares.BioOpticWiring, 320),
                       Consumption(wares.EnergyCells, 480),
                       Consumption(wares.FusionReactors, 40),
                       Consumption(wares.ReinforcedMetalPlating, 160)],

                'ar': [Consumption(wares.EnergyCells, 480),
                       Consumption(wares.FusionReactors, 40),
                       Consumption(wares.PlasmaPumps, 240),
                       Consumption(wares.ReinforcedMetalPlating, 160)]}

ShieldFacility = Module(names, productions, consumptions)
