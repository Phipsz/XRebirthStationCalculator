from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Licensed Distillery',
         'L049': 'Lizensierte Destille'}

smodules = [modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179),
            modules.LiquorStill(production_method='ar', efficiency=179)]

OL_LicensedDistillery = Station(names, smodules)
