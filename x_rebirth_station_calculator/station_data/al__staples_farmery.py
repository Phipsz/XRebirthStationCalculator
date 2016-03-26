from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Staples Farmery',
         'L049': 'Grundnahrungsmittelfarm'}

smodules = [(modules.FoodstuffFac, 4),
            (modules.LiquorStill, 2)]

productions = [Production(wares.FoodRations, 48000, 146.25),
               Production(wares.Spacefuel, 3840.0, 156.0)]

consumptions = [Consumption(wares.EnergyCells, 11520.0),
                Consumption(wares.Meat, 4800.0),
                Consumption(wares.Spices, 5760.0),
                Consumption(wares.Water, 3840.0),
                Consumption(wares.Wheat, 19680.0)]

AL_StaplesFarmery = Station(names, smodules, productions, consumptions)
