from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'R&D Chem Lab',
         'L049': 'F&E Chem-Lab'}

smodules = [(modules.ChemRefinery, 2),
            (modules.GelFactory, 2),
            (modules.PPPPlant, 2),
            (modules.QTubeYFab, 2)]

productions = [Production(wares.ChemicalCompounds, 3360.0, 163.0),
               Production(wares.BioElectricNeuronGel, 1280.0, 155.5),
               Production(wares.PlasmaPumps, 480.0, 158.0),
               Production(wares.QuantumTubes, 480.0, 163.0)]

consumptions = [Consumption(wares.BoFu, 2340.0),
                Consumption(wares.ChemicalCompounds, 2400.0),
                Consumption(wares.CutCrystals, 640.0),
                Consumption(wares.EnergyCells, 9600.0),
                Consumption(wares.Ions, 1920.0),
                Consumption(wares.IonCells, 2880.0),
                Consumption(wares.MedicalSupplies, 1000.00, True),
                Consumption(wares.NividiumCubes, 720.0),
                Consumption(wares.Plasma, 2400.0),
                Consumption(wares.PlasmaCells, 3200.0),
                Consumption(wares.RefinedMetals, 1800.0),
                Consumption(wares.SiliconWafers, 2560.0),
                Consumption(wares.Spacefuel, 800.0, True),
                Consumption(wares.Water, 2560.0)]

OL_RDChemLab = Station(names, smodules, productions, consumptions)
