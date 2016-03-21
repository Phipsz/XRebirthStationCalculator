from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Crystal Supplier',
         'L049': 'Kristall-Zulieferer'}

smodules = [(modules.CrystalCuttery, 3),
            (modules.CubePlant, 3)]

productions = [Production(wares.CutCrystals, 7920.0, 140.0),
               Production(wares.NividiumCubes, 7920.0, 139.0)]

consumptions = [Consumption(wares.Crystals, 7200.0),
                Consumption(wares.EnergyCells, 11520.0),
                Consumption(wares.FoodRations, 8640.0),
                Consumption(wares.Narcotics, 720.0, True),
                Consumption(wares.Nividium, 7200.0),
                Consumption(wares.Spacefuel, 144.0, True),
                Consumption(wares.Water, 2880)]

AL_CrystalSupplier = Station(names, smodules, productions, consumptions)
