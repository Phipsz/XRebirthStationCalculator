import os.path
import glob
import re

_modules = glob.glob(os.path.dirname(__file__)+"/*.py")
_submodules = [os.path.basename(f)[:-3] for f in _modules if os.path.isfile(f)]
for _module in _submodules:
    with open(os.path.dirname(__file__) + '/' + _module + '.py') as mod:
        _data = mod.read()
        _matchObj = re.search(r'^(\S*) = Station\(.*', _data,
                              re.UNICODE | re.MULTILINE)
        if _matchObj:
            _name = _matchObj.group(1)
            locals()[_name] = __import__('station_data.' + _module,
                                         globals(), locals(), [_name])
            locals()[_name] = getattr(locals()[_name], _name)
        del(_matchObj)
        del(_data)

del(_modules)
del(_submodules)
