from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Foodstuffs Supply',
         'L049': 'Nahrungsmittel-Zulieferer'}

smodules = [(modules.FoodstuffFac, 2),
            (modules.ValleyForge, 2),
            (modules.LiquorStill, 1),
            (modules.ArgnuParadise, 1),
            (modules.SpiceTubes, 1)]

productions = [Production(wares.FoodRations, 24000, 145.5),
               Production(wares.Wheat, 10800.0, 145.0),
               Production(wares.Spacefuel, 1920.0, 144.5),
               Production(wares.Meat, 1920.0, 145.0),
               Production(wares.Spices, 3200.0, 144.0)]

consumptions = [Consumption(wares.EnergyCells, 8480.0),
                Consumption(wares.Meat, 2400.0),
                Consumption(wares.Spices, 2880.0),
                Consumption(wares.Water, 13200.0),
                Consumption(wares.Wheat, 11520.0)]

AL_FoodstuffsSupply = Station(names, smodules, productions, consumptions)
