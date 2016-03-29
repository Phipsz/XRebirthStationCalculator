from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Pharma Platform',
         'L049': 'Pharma-Platform'}

productions = {'universal': [Production(wares.MedicalSupplies, 1440)]}

consumptions = {'universal': [Consumption(wares.EnergyCells, 720),
                              Consumption(wares.Narcotics, 1440),
                              Consumption(wares.Spaceweed, 960)]}

PharmaPlatform = Module(names, productions, consumptions)
