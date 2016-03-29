from x_rebirth_station_calculator.station_data.station_base import Module
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption
from x_rebirth_station_calculator.station_data import wares

names = {'L044': 'EM Fac Tower',
         'L049': 'EM-Fabrikturm'}

productions = {'ar': [Production(wares.EMSpectrometer, 120)]}

consumptions = {'ar': [Consumption(wares.BioElectricNeuronGel, 80),
                       Consumption(wares.BoFu, 160),
                       Consumption(wares.ChemicalCompounds, 80),
                       Consumption(wares.CutCrystals, 640),
                       Consumption(wares.EnergyCells, 640),
                       Consumption(wares.QuantumTubes, 40),
                       Consumption(wares.RefinedMetals, 320),
                       Consumption(wares.SiliconWafers, 960),
                       Consumption(wares.MedicalSupplies, 240, True),
                       Consumption(wares.Spacefuel, 80, True)]}

EMFacTower = Module(names, productions, consumptions)
