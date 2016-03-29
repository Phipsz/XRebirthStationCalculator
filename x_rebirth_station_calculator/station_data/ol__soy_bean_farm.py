from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Soy Bean Farm',
         'L049': 'Sojabohnenplantage'}

smodules = [modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194),
            modules.SoyBeanery(production_method='ar', efficiency=194)]

OL_SoyBeanFarm = Station(names, smodules)
