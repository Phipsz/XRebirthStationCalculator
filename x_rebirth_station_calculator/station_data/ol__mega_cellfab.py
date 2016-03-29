from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Mega Cellfab',
         'L049': 'Mega-Zell-Fab'}

smodules = [modules.PlasmaCyclotron(production_method='ar', efficiency=165),
            modules.PlasmaCyclotron(production_method='ar', efficiency=165),
            modules.PlasmaCyclotron(production_method='ar', efficiency=165),
            modules.IonCellPlant(production_method='ar', efficiency=158),
            modules.IonCellPlant(production_method='ar', efficiency=157),
            modules.IonCellPlant(production_method='ar', efficiency=157),
            modules.AMCyclotron(production_method='ar', efficiency=149),
            modules.AMCyclotron(production_method='ar', efficiency=149),
            modules.AMCyclotron(production_method='ar', efficiency=149)]

OL_MegaCellfab = Station(names, smodules)
