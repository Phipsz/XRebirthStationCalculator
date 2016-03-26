from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Tech Laboratory',
         'L049': 'Technologie-Lab'}

smodules = [(modules.ChemRefinery, 2),
            (modules.ChipFab, 2),
            (modules.BioOpticsFac, 2),
            (modules.QTubeYFab, 2)]

productions = [Production(wares.ChemicalCompounds, 3360.0, 142.5),
               Production(wares.Microchips, 1280.0, 140.5),
               Production(wares.BioOpticWiring, 480.0, 140.5),
               Production(wares.QuantumTubes, 480.0, 142.0)]

consumptions = [Consumption(wares.ChemicalCompounds, 1560.0),
                Consumption(wares.EnergyCells, 9600.0),
                Consumption(wares.FoodRations, 4320.0),
                Consumption(wares.Ions, 1920.0),
                Consumption(wares.IonCells, 2880.0),
                Consumption(wares.MedicalSupplies, 1080.00, True),
                Consumption(wares.NividiumCubes, 720.0),
                Consumption(wares.Plasma, 2880.0),
                Consumption(wares.PlasmaCells, 2560.0),
                Consumption(wares.RefinedMetals, 2080.0),
                Consumption(wares.SiliconWafers, 3200.0),
                Consumption(wares.Spacefuel, 1020.0, True)]

AL_TechLaboratory = Station(names, smodules, productions, consumptions)
