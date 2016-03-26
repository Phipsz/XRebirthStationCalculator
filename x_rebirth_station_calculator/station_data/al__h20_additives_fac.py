from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'H2O Additives Fac',
         'L049': 'H2O Anreicherungs-Anl'}

smodules = [(modules.CondenserStill, 4),
            (modules.IceRefinery, 4)]

productions = [Production(wares.Water, 57600.0, 144.5),
               Production(wares.Ice, 12000.0, 122.0)]

consumptions = [Consumption(wares.EnergyCells, 19200.0),
                Consumption(wares.Ice, 48000.0)]

AL_H2OAdditivesFac = Station(names, smodules, productions, consumptions)
