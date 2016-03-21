from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Technology Megacomplex',
         'L049': 'Techno-Megaplex'}

smodules = [(modules.QTubeYFab, 2),
            (modules.PPPPlant, 2),
            (modules.EMFacTower, 1),
            (modules.WarheadForge, 1)]

productions = [Production(wares.QuantumTubes, 480.0, 160.0),
               Production(wares.PlasmaPumps, 480.0, 153.5),
               Production(wares.EMSpectrometer, 120.0, 152.0),
               Production(wares.WarheadComponents, 40.0, 152.0)]

consumptions = [Consumption(wares.AntimatterCells, 440),
                Consumption(wares.BioElectricNeuronGel, 120.0),
                Consumption(wares.BoFu, 1340.0),
                Consumption(wares.ChemicalCompounds, 1240.0),
                Consumption(wares.CutCrystals, 1280.0),
                Consumption(wares.EMSpectrometer, 20.0),
                Consumption(wares.EnergyCells, 5720.0),
                Consumption(wares.MedicalSupplies, 820.00, True),
                Consumption(wares.NividiumCubes, 720.0),
                Consumption(wares.PlasmaCells, 1280.0),
                Consumption(wares.QuantumTubes, 40.0),
                Consumption(wares.RefinedMetals, 2340.0),
                Consumption(wares.SiliconWafers, 960.0),
                Consumption(wares.Spacefuel, 380.0, True)]

OL_TechnologyMegacomplex = Station(names, smodules, productions, consumptions)
