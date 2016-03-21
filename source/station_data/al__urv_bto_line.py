from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'URV BTO Line',
         'L049': 'URV-Auftragsfertigung'}

smodules = [(modules.URVWharf, 4)]

productions = [Production(wares.AssaultURV, 6.16, 109.25),
               Production(wares.CargolifterURV, 18.48, 109.25),
               Production(wares.ConstructionURV, 9.48, 109.25),
               Production(wares.InterceptorURVMk1, 14.76, 109.25),
               Production(wares.InterceptorURVMk2, 4.32, 109.25),
               Production(wares.IntrepidURVMk1, 11.08, 109.25),
               Production(wares.IntrepidURVMk2, 3.08, 109.25),
               Production(wares.OverrunURVMk1, 8.6, 109.25),
               Production(wares.OverrunURVMk2, 2.48, 109.25),
               Production(wares.ScoopCollectorURVMk1, 16.0, 109.25),
               Production(wares.ScoopCollectorURVMk2, 4.92, 109.25),
               Production(wares.SurfaceMinerURVMk1, 17.24, 109.25),
               Production(wares.SurfaceMinerURVMk2, 4.92, 109.25)]

consumptions = [Consumption(wares.BioOpticWiring, 499.0),
                Consumption(wares.EnergyCells, 1545.0),
                Consumption(wares.FoodRations, 1060.0),
                Consumption(wares.FusionReactors, 22.0),
                Consumption(wares.PodkletnovGenerators, 33.0),
                Consumption(wares.Microchips, 95.0),
                Consumption(wares.PlasmaFlowRegulators, 35.0),
                Consumption(wares.ReinforcedMetalPlating, 63.0),
                Consumption(wares.ScanningArray, 162.0)]

AL_URVBTOLine = Station(names, smodules, productions, consumptions)
