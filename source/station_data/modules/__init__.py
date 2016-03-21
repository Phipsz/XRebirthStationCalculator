import os.path
import glob
import re
import importlib

_modules = glob.glob(os.path.dirname(__file__)+"/*.py")
_submodules = [os.path.basename(f)[:-3] for f in _modules if os.path.isfile(f)]
for _module in _submodules:
    with open(os.path.dirname(__file__) + '/' + _module + '.py') as _mod:
        _data = _mod.read()
        _matchObj = re.search(r'^(\S*) = Module\(.*', _data,
                              re.UNICODE | re.MULTILINE)
        if _matchObj:
            _name = _matchObj.group(1)
            _modname = 'station_data.modules.' + _module
            _mod = importlib.import_module(_modname)
            locals()[_name] = getattr(_mod, _name)
            del(_name)
            del(_modname)
            del(_mod)
        del(_data)
        del(_matchObj)

del(_modules)
del(_submodules)
