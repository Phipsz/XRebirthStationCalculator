from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'High Tech Fab',
         'L049': 'High-Tech-Fab'}

smodules = [(modules.ChipFab, 2),
            (modules.BioOpticsFac, 2),
            (modules.ScannArFacility, 2)]

productions = [Production(wares.Microchips, 1280.0, 142.5),
               Production(wares.BioOpticWiring, 480.0, 140.0),
               Production(wares.ScanningArray, 80.0, 140.5)]

consumptions = [Consumption(wares.ChemicalCompounds, 1120.0),
                Consumption(wares.CutCrystals, 1280.0),
                Consumption(wares.EnergyCells, 5120.0),
                Consumption(wares.FoodRations, 2720.0),
                Consumption(wares.MedicalSupplies, 800.00, True),
                Consumption(wares.Microchips, 160.0),
                Consumption(wares.PlasmaCells, 640.0),
                Consumption(wares.QuantumTubes, 80.0),
                Consumption(wares.RefinedMetals, 1280.0),
                Consumption(wares.Spacefuel, 720.0, True),
                Consumption(wares.SiliconWafers, 4000.0)]

AL_HighTechFab = Station(names, smodules, productions, consumptions)
