from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Solar Energy Array',
         'L049': 'Solarenergiekollektor'}

smodules = [modules.SolarConverter(production_method='ar', efficiency=141),
            modules.SolarConverter(production_method='ar', efficiency=141),
            modules.SolarConverter(production_method='ar', efficiency=141),
            modules.SolarConverter(production_method='ar', efficiency=141),
            modules.SolarConverter(production_method='ar', efficiency=149),
            modules.SolarConverter(production_method='ar', efficiency=149),
            modules.SolarConverter(production_method='ar', efficiency=149),
            modules.SolarConverter(production_method='ar', efficiency=149)]

OL_SolarEnergyArray = Station(names, smodules)
