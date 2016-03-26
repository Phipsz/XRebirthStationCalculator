from x_rebirth_station_calculator.station_data import modules
from x_rebirth_station_calculator.station_data import wares
from x_rebirth_station_calculator.station_data.station_base import Station
from x_rebirth_station_calculator.station_data.station_base import Production
from x_rebirth_station_calculator.station_data.station_base import Consumption

names = {'L044': 'Hardware Supplier',
         'L049': 'Material-Zulieferer'}

smodules = [(modules.PlateFoundry, 2),
            (modules.SteelRefinery, 3),
            (modules.ChemRefinery, 2)]

productions = [Production(wares.ReinforcedMetalPlating, 720.0, 153.0),
               Production(wares.RefinedMetals, 3600.0, 153.0),
               Production(wares.ChemicalCompounds, 3360.0, 151.0)]

consumptions = [Consumption(wares.ChemicalCompounds, 480.0),
                Consumption(wares.EnergyCells, 15360.0),
                Consumption(wares.BoFu, 3700.0),
                Consumption(wares.Ions, 1920.0),
                Consumption(wares.IonCells, 2880.0),
                Consumption(wares.MedicalSupplies, 680.0, True),
                Consumption(wares.Narcotics, 360.0, True),
                Consumption(wares.NividiumCubes, 1280.0),
                Consumption(wares.Ore, 7200.0),
                Consumption(wares.Plasma, 2400.0),
                Consumption(wares.PlasmaCells, 1920.0),
                Consumption(wares.RefinedMetals, 3920.0),
                Consumption(wares.Spacefuel, 2556.0, True)]

OL_HardwareSupplier = Station(names, smodules, productions, consumptions)
