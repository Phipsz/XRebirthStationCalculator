from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Plasma Tech',
         'L049': 'Plasma-Tech-Anlage'}

productions = {'al': [Production(wares.PlasmaFlowRegulators, 40)],
               'ar': [Production(wares.PlasmaFlowRegulators, 40)]}

consumptions = {'al': [Consumption(wares.EnergyCells, 1200),
                       Consumption(wares.FoodRations, 400),
                       Consumption(wares.Microchips, 240),
                       Consumption(wares.PlasmaCells, 480),
                       Consumption(wares.QuantumTubes, 160),
                       Consumption(wares.MedicalSupplies, 320, True),
                       Consumption(wares.Spacefuel, 180, True)],

                'ar': [Consumption(wares.BioElectricNeuronGel, 180),
                       Consumption(wares.BoFu, 340),
                       Consumption(wares.EnergyCells, 1600),
                       Consumption(wares.QuantumTubes, 180),
                       Consumption(wares.Narcotics, 380, True),
                       Consumption(wares.Spacefuel, 160, True)]}

PlasmaTech = Module(names, productions, consumptions)
