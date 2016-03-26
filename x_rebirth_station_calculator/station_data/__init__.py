import os.path
import glob
import re
import importlib

station_list = list()
name_mappings = dict()

_modules = glob.glob(os.path.dirname(__file__)+"/*.py")
_submodules = [os.path.basename(f)[:-3] for f in _modules if os.path.isfile(f)]
for _module in _submodules:
    with open(os.path.dirname(__file__) + '/' + _module + '.py',
              encoding='utf-8') as _mod:
        _data = _mod.read()
        _matchObj = re.search(r'^(\S*) = Station\(.*', _data,
                              re.UNICODE | re.MULTILINE)
        if _matchObj:
            _name = _matchObj.group(1)
            _modname = 'x_rebirth_station_calculator.station_data.' + _module
            _mod = importlib.import_module(_modname)
            locals()[_name] = getattr(_mod, _name)
            station_list.append(locals()[_name])
            name_mappings[locals()[_name].get_name()] = _name
            del(_name)
            del(_modname)
            del(_mod)
        del(_data)
        del(_matchObj)

del(_modules)
del(_submodules)
