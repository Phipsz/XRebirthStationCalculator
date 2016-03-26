from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Crystal Refinery',
         'L049': 'Kristall-Raffinerie'}

smodules = [(modules.CrystalCuttery, 3),
            (modules.CubePlant, 3)]

productions = [Production(wares.CutCrystals, 7920.0, 156.0),
               Production(wares.NividiumCubes, 7920.0, 153.33)]

consumptions = [Consumption(wares.Crystals, 7200.0),
                Consumption(wares.EnergyCells, 10080.0),
                Consumption(wares.BoFu, 4320.0),
                Consumption(wares.Narcotics, 720.0, True),
                Consumption(wares.Nividium, 7200.0),
                Consumption(wares.Spacefuel, 144.0, True),
                Consumption(wares.Water, 2880)]

OL_CrystalRefinery = Station(names, smodules, productions, consumptions)
