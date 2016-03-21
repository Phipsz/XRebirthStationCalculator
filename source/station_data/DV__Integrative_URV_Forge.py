from station_data import modules
from station_data import wares
from station_datstation_data.station_base import Station
from station_datstation_data.station_base import Production
from station_datstation_data.station_base import Consumption

names = {'L044': 'Integrative URV Forge',
         'L049': 'Integrative URV-Montage'}

smodules = [(modules.SteelRefinery, 2),
            (modules.WaferPlant, 2),
            (modules.URFWharf, 2)]

productions = [Production(wares.RefinedMetals, 2400.0, 148.5),
               Production(wares.SiliconWafers, 2640.0, 143.5),
               Production(wares.InterceptorURVMk1, 5.34, 110.0),
               Production(wares.CargolifterURV, 9.34, 110.0),
               Production(wares.ConstructionURV, 4.0, 110.0),
               Production(wares.ScoopCollectorURVMk1, 4.0, 110.0),
               Production(wares.SurfaceMinerURVMk1, 5.34, 110.0)]

consumptions = [Consumption(wares.CutCrystals, 480.0),
                Consumption(wares.Crystals, 6964.0),
                Consumption(wares.EnergyCells, 9598.0),
                Consumption(wares.FoodRations, 6746.0),
                Consumption(wares.MedicalSupplies, 24.0, True),
                Consumption(wares.Narcotics, 480.0, True),
                Consumption(wares.Nividium, 6510.0),
                Consumption(wares.Ore, 17062.0),
                Consumption(wares.Silicon, 15700.0),
                Consumption(wares.Spacefuel, 48.0, True)]

DV_IntegrativeURVForge = Station(names, smodules, productions, consumptions)
