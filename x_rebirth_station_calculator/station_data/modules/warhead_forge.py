from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'Warhead Forge',
         'L049': 'Gefechtskopfschmiede'}

productions = {'al': [Production(wares.WarheadComponents, 40)],
               'ar': [Production(wares.WarheadComponents, 40)]}

consumptions = {'al': [Consumption(wares.AntimatterCells, 480),
                       Consumption(wares.ChemicalCompounds, 40),
                       Consumption(wares.EnergyCells, 480),
                       Consumption(wares.FoodRations, 320),
                       Consumption(wares.Microchips, 40),
                       Consumption(wares.PlasmaCells, 160),
                       Consumption(wares.QuantumTubes, 20),
                       Consumption(wares.RefinedMetals, 160),
                       Consumption(wares.MedicalSupplies, 100, True),
                       Consumption(wares.Spacefuel, 80, True)],

                'ar': [Consumption(wares.AntimatterCells, 440),
                       Consumption(wares.BioElectricNeuronGel, 40),
                       Consumption(wares.BoFu, 160),
                       Consumption(wares.ChemicalCompounds, 40),
                       Consumption(wares.EMSpectrometer, 20),
                       Consumption(wares.EnergyCells, 760),
                       Consumption(wares.RefinedMetals, 220),
                       Consumption(wares.MedicalSupplies, 100, True),
                       Consumption(wares.Spacefuel, 100, True)]}

WarheadForge = Module(names, productions, consumptions)
