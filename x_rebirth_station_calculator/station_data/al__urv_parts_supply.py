from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data.station_base import Station

names = {'L044': 'URV Parts Supply',
         'L049': 'URV-Teilezulieferer'}

smodules = [modules.URVWharf(production_method='al', efficiency=128),
            modules.ChipFab(production_method='al', efficiency=152),
            modules.BioOpticsFac(production_method='al', efficiency=157),
            modules.FusionCoreFac(production_method='al', efficiency=152),
            modules.PlasmaTech(production_method='al', efficiency=153),
            modules.PodkletnovFab(production_method='al', efficiency=153),
            modules.ScannArFacility(production_method='al', efficiency=156)]

AL_URVPartsSupply = Station(names, smodules)
