from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Licensed Distillery',
         'L049': 'Lizensierte Destille'}

smodules = [(modules.LiquorStill, 4)]

productions = [Production(wares.Spacefuel, 7680.0, 171.5)]

consumptions = [Consumption(wares.EnergyCells, 3840.0),
                Consumption(wares.Plankton, 960.0),
                Consumption(wares.Spices, 1920.0),
                Consumption(wares.Water, 7680.0)]

OL_LicensedDistillery = Station(names, smodules, productions, consumptions)
