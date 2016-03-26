from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Ship Tech Fab',
         'L049': 'Schiffstech Fab'}

smodules = [(modules.FusionCoreFac, 2),
            (modules.PlasmaTech, 2),
            (modules.PodkletnovFab, 2)]

productions = [Production(wares.FusionReactors, 240.0, 144.5),
               Production(wares.PlasmaFlowRegulators, 80.0, 139.0),
               Production(wares.PodkletnovGenerators, 144.0, 141.0)]

consumptions = [Consumption(wares.AntimatterCells, 5520.0),
                Consumption(wares.EnergyCells, 7584.0),
                Consumption(wares.FoodRations, 2720.0),
                Consumption(wares.IonCells, 1536.0),
                Consumption(wares.MedicalSupplies, 2416.0, True),
                Consumption(wares.Microchips, 1248.0),
                Consumption(wares.NividiumCubes, 2592.0),
                Consumption(wares.PlasmaCells, 960.0),
                Consumption(wares.QuantumTubes, 872.0),
                Consumption(wares.RefinedMetals, 1200.0),
                Consumption(wares.SiliconWafers, 2880.0),
                Consumption(wares.Spacefuel, 1824.0, True)]

AL_ShipTechFab = Station(names, smodules, productions, consumptions)
