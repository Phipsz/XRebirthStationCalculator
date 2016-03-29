from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Gel Factory',
         'L049': 'Gelfabrik'}

productions = {'ar': [Production(wares.BioElectricNeuronGel, 640)]}

consumptions = {'ar': [Consumption(wares.BoFu, 240),
                       Consumption(wares.ChemicalCompounds, 640),
                       Consumption(wares.EnergyCells, 960),
                       Consumption(wares.SiliconWafers, 1280),
                       Consumption(wares.Water, 1280),
                       Consumption(wares.MedicalSupplies, 80, True),
                       Consumption(wares.Spacefuel, 240, True)]}

GelFactory = Module(names, productions, consumptions)
