from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'PPP Plant',
         'L049': 'PPP-Anlage'}

productions = {'ar': [Production(wares.PlasmaPumps, 240)]}

consumptions = {'ar': [Consumption(wares.BoFu, 240),
                       Consumption(wares.ChemicalCompounds, 320),
                       Consumption(wares.CutCrystals, 320),
                       Consumption(wares.EnergyCells, 960),
                       Consumption(wares.PlasmaCells, 640),
                       Consumption(wares.MedicalSupplies, 120, True),
                       Consumption(wares.Spacefuel, 40, True)]}

PPPPlant = Module(names, productions, consumptions)
