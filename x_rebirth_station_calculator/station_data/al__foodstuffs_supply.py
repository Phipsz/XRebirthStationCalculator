from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'Foodstuffs Supply',
         'L049': 'Nahrungsmittel-Zulieferer'}

smodules = [modules.FoodstuffFac(production_method='al', efficiency=147),
            modules.FoodstuffFac(production_method='al', efficiency=143),
            modules.ValleyForge(production_method='al', efficiency=144),
            modules.ValleyForge(production_method='al', efficiency=144),
            modules.LiquorStill(production_method='al', efficiency=155),
            modules.ArgnuParadise(production_method='al', efficiency=144),
            modules.SpiceTubes(efficiency=143)]

AL_FoodstuffsSupply = Station(names, smodules)
