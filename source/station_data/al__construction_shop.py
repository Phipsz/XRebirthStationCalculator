from station_data import modules
from station_data import wares
from station_data.station_base import Station
from station_data.station_base import Production
from station_data.station_base import Consumption

names = {'L044': 'Construction Shop',
         'L049': 'Baumarkt'}

smodules = [(modules.PlateFoundry, 3),
            (modules.SteelRefinery, 3),
            (modules.ChemRefinery, 2)]

productions = [Production(wares.ReinforcedMetalPlating, 1200.0, 142.67),
               Production(wares.RefinedMetals, 3600.0, 141.33),
               Production(wares.ChemicalCompounds, 3360.0, 140.5)]

consumptions = [Consumption(wares.ChemicalCompounds, 1440.0),
                Consumption(wares.EnergyCells, 14400.0),
                Consumption(wares.FoodRations, 8640.0),
                Consumption(wares.Ions, 1920.0),
                Consumption(wares.IonCells, 2880.0),
                Consumption(wares.MedicalSupplies, 840.0, True),
                Consumption(wares.Narcotics, 360.0, True),
                Consumption(wares.NividiumCubes, 1920.0),
                Consumption(wares.Ore, 7200.0),
                Consumption(wares.Plasma, 2880.0),
                Consumption(wares.PlasmaCells, 1920.0),
                Consumption(wares.RefinedMetals, 7200.0),
                Consumption(wares.Spacefuel, 5076.0, True)]

AL_ConstructionShop = Station(names, smodules, productions, consumptions)
