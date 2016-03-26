from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Metalworks Yard',
         'L049': 'Metallgießerei'}

smodules = [(modules.SteelRefinery, 3),
            (modules.WaferPlant, 3)]

productions = [Production(wares.RefinedMetals, 2400.0, 143.0),
               Production(wares.SiliconWafers, 2640.0, 141.0)]

consumptions = [Consumption(wares.CutCrystals, 720.0),
                Consumption(wares.EnergyCells, 12240.0),
                Consumption(wares.FoodRations, 8640.0),
                Consumption(wares.MedicalSupplies, 36.0, True),
                Consumption(wares.Narcotics, 720.0, True),
                Consumption(wares.Ore, 7200.0),
                Consumption(wares.Silicon, 7200.0),
                Consumption(wares.Spacefuel, 72.0, True)]

AL_MetalworksYard = Station(names, smodules, productions, consumptions)
