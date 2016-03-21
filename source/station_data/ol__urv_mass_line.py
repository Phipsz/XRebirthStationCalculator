from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'URV Mass Line',
         'L049': 'URV-Massenfertigung'}

smodules = [(modules.URVWharf, 4)]

productions = [Production(wares.AssaultURV, 6.16, 116.5),
               Production(wares.CargolifterURV, 18.48, 116.5),
               Production(wares.ConstructionURV, 9.48, 116.5),
               Production(wares.InterceptorURVMk1, 14.76, 116.5),
               Production(wares.InterceptorURVMk2, 4.32, 116.5),
               Production(wares.IntrepidURVMk1, 11.08, 116.5),
               Production(wares.IntrepidURVMk2, 3.08, 116.5),
               Production(wares.OverrunURVMk1, 8.6, 116.5),
               Production(wares.OverrunURVMk2, 2.48, 116.5),
               Production(wares.ScoopCollectorURVMk1, 16.0, 116.5),
               Production(wares.ScoopCollectorURVMk2, 4.92, 116.5),
               Production(wares.SurfaceMinerURVMk1, 17.24, 116.5),
               Production(wares.SurfaceMinerURVMk2, 4.92, 116.5)]

consumptions = [Consumption(wares.BioElectricNeuronGel, 397.0),
                Consumption(wares.BoFu, 532.0),
                Consumption(wares.EMSpectrometer, 178.0),
                Consumption(wares.EnergyCells, 1534.0),
                Consumption(wares.FusionReactors, 22.0),
                Consumption(wares.PodkletnovGenerators, 33.0),
                Consumption(wares.PlasmaFlowRegulators, 35.0),
                Consumption(wares.PlasmaPumps, 300.0),
                Consumption(wares.ReinforcedMetalPlating, 62.0)]

OL_URVMassLine = Station(names, smodules, productions, consumptions)
