from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Staples Farmery',
         'L049': 'Grundnahrungsmittelfarm'}

smodules = [modules.FoodstuffFac(production_method='al', efficiency=150),
            modules.FoodstuffFac(production_method='al', efficiency=146),
            modules.FoodstuffFac(production_method='al', efficiency=147),
            modules.FoodstuffFac(production_method='al', efficiency=142),
            modules.LiquorStill(production_method='al', efficiency=160),
            modules.LiquorStill(production_method='al', efficiency=153)]

AL_StaplesFarmery = Station(names, smodules)
