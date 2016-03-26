from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'TechnoCore Parts',
         'L049': 'TechnoCore-Teile'}

smodules = [(modules.GelFactory, 2),
            (modules.EMFacTower, 2),
            (modules.PPPPlant, 2)]

productions = [Production(wares.BioElectricNeuronGel, 1280.0, 155.5),
               Production(wares.EMSpectrometer, 240.0, 156.0),
               Production(wares.PlasmaPumps, 480.0, 156.0)]

consumptions = [Consumption(wares.BioElectricNeuronGel, 160.0),
                Consumption(wares.BoFu, 1280.0),
                Consumption(wares.ChemicalCompounds, 2080.0),
                Consumption(wares.CutCrystals, 1920.0),
                Consumption(wares.EnergyCells, 5120.0),
                Consumption(wares.MedicalSupplies, 880.00, True),
                Consumption(wares.PlasmaCells, 1280.0),
                Consumption(wares.QuantumTubes, 80.0),
                Consumption(wares.RefinedMetals, 640.0),
                Consumption(wares.SiliconWafers, 4480.0),
                Consumption(wares.Spacefuel, 720.0, True),
                Consumption(wares.Water, 2560.0)]

OL_TechnoCoreParts = Station(names, smodules, productions, consumptions)
