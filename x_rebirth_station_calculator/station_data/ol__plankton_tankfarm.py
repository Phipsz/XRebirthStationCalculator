from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Plankton Tankfarm',
         'L049': 'Plankton-Tankfarm'}

smodules = [(modules.PlanktonTank, 6)]

productions = [Production(wares.Plankton, 34560.0, 176.17)]

consumptions = [Consumption(wares.EnergyCells, 2880.0),
                Consumption(wares.Water, 17280.0)]

OL_PlanktonTankfarm = Station(names, smodules, productions, consumptions)
