from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Techno-Complex',
         'L049': 'Technoplex'}

smodules = [(modules.QTubeYFab, 2),
            (modules.BioOpticsFac, 2),
            (modules.ScannArFacility, 1),
            (modules.WarheadForge, 1)]

productions = [Production(wares.QuantumTubes, 480.0, 143.5),
               Production(wares.BioOpticWiring, 480.0, 143.0),
               Production(wares.ScanningArray, 80.0, 142.0),
               Production(wares.WarheadComponents, 40.0, 139.0)]

consumptions = [Consumption(wares.AntimatterCells, 480),
                Consumption(wares.ChemicalCompounds, 1360.0),
                Consumption(wares.CutCrystals, 640.0),
                Consumption(wares.EnergyCells, 5440.0),
                Consumption(wares.FoodRations, 2640.0),
                Consumption(wares.MedicalSupplies, 660.00, True),
                Consumption(wares.Microchips, 120),
                Consumption(wares.NividiumCubes, 720.0),
                Consumption(wares.PlasmaCells, 800.0),
                Consumption(wares.RefinedMetals, 1920.0),
                Consumption(wares.SiliconWafers, 400.0),
                Consumption(wares.Spacefuel, 740.0, True)]

AL_TechnoComplex = Station(names, smodules, productions, consumptions)
