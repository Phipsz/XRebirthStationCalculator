from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Solar Energy Array',
         'L049': 'Solarenergiekollektor'}

smodules = [(modules.SolarConverter, 4)]

productions = [Production(wares.EnergyCells, 67200.0, 152.0)]

consumptions = [Consumption(wares.BoFu, 192.0, True)]

OL_SolarEnergyArray = Station(names, smodules, productions, consumptions)
