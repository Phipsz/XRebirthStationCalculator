from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Mega-Tank Farm',
         'L049': 'Megaaquarium-Farm'}

smodules = [modules.SpiceTubes(efficiency=159),
            modules.SpiceTubes(efficiency=159),
            modules.PlanktonTank(production_method='ar', efficiency=160),
            modules.PlanktonTank(production_method='ar', efficiency=160),
            modules.PlanktonTank(production_method='ar', efficiency=160),
            modules.PlanktonTank(production_method='ar', efficiency=160),
            modules.SoyBeanery(production_method='ar', efficiency=178),
            modules.SoyBeanery(production_method='ar', efficiency=178),
            modules.SoyBeanery(production_method='ar', efficiency=178),
            modules.SoyBeanery(production_method='ar', efficiency=178)]

OL_MegaTankFarm = Station(names, smodules)
