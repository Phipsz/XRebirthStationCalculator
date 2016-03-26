from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Pharma Lab',
         'L049': 'Pharma-Lab'}

smodules = [(modules.NarcoticsLab, 4),
            (modules.PharmaPlatform, 4),
            (modules.HerbGarden, 4)]

productions = [Production(wares.Narcotics, 5760.0, 151.0),
               Production(wares.MedicalSupplies, 5760.0, 152.0),
               Production(wares.Spaceweed, 4800.0, 152.75)]

consumptions = [Consumption(wares.EnergyCells, 7680.0),
                Consumption(wares.Narcotics, 5760.0),
                Consumption(wares.Spaceweed, 8640.0),
                Consumption(wares.Spacefuel, 960.0),
                Consumption(wares.Water, 4800.0)]

OL_PharmaLab = Station(names, smodules, productions, consumptions)
