from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Chem Refinery',
         'L049': 'Chemie-Raffinerie'}

productions = {'al': [Production(wares.ChemicalCompounds, 1680)],
               'ar': [Production(wares.ChemicalCompounds, 1680)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.FoodRations, 720),
                       Consumption(wares.IonCells, 1440),
                       Consumption(wares.Ions, 960),
                       Consumption(wares.Plasma, 1440),
                       Consumption(wares.PlasmaCells, 960),
                       Consumption(wares.MedicalSupplies, 180, True),
                       Consumption(wares.Spacefuel, 120, True)],

                'ar': [Consumption(wares.BoFu, 420),
                       Consumption(wares.EnergyCells, 1680),
                       Consumption(wares.IonCells, 1440),
                       Consumption(wares.Ions, 960),
                       Consumption(wares.Plasma, 1200),
                       Consumption(wares.PlasmaCells, 960),
                       Consumption(wares.MedicalSupplies, 180, True),
                       Consumption(wares.Spacefuel, 60, True)]}

ChemRefinery = Module(names, productions, consumptions)
