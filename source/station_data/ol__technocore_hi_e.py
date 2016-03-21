from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'TechnoCore Hi-E',
         'L049': 'TechnoCore H-E'}

smodules = [(modules.FusionCoreFac, 2),
            (modules.PodkletnovFab, 2),
            (modules.PlasmaTech, 2)]

productions = [Production(wares.FusionReactors, 240.0, 147.0),
               Production(wares.PodkletnovGenerators, 144.0, 146.5),
               Production(wares.PlasmaFlowRegulators, 80.0, 145.0)]

consumptions = [Consumption(wares.AntimatterCells, 5472.0),
                Consumption(wares.BioElectricNeuronGel, 972.0),
                Consumption(wares.BoFu, 1904.0),
                Consumption(wares.EnergyCells, 7520.0),
                Consumption(wares.IonCells, 1536.0),
                Consumption(wares.MedicalSupplies, 1992.0, True),
                Consumption(wares.Narcotics, 760.0, True),
                Consumption(wares.NividiumCubes, 2784.0),
                Consumption(wares.QuantumTubes, 852.0),
                Consumption(wares.RefinedMetals, 1440.0),
                Consumption(wares.SiliconWafers, 2976.0),
                Consumption(wares.Spacefuel, 1028.0, True)]

OL_TechnoCoreHiE = Station(names, smodules, productions, consumptions)
