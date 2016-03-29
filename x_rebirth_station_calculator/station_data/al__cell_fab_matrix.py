from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Cell Fab Matrix',
         'L049': 'Zell-Fab-Matrix'}

smodules = [modules.PlasmaCyclotron(production_method='al', efficiency=146),
            modules.PlasmaCyclotron(production_method='al', efficiency=146),
            modules.IonCellPlant(production_method='al', efficiency=141),
            modules.IonCellPlant(production_method='al', efficiency=141),
            modules.AMCyclotron(production_method='al', efficiency=141),
            modules.AMCyclotron(production_method='al', efficiency=141)]

AL_CellFabMatrix = Station(names, smodules)
