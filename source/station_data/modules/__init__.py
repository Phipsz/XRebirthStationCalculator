import os.path
import glob
import re

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
submodules = [os.path.basename(f)[:-3] for f in modules if os.path.isfile(f)]
for module in submodules:
    names = dict()
    with open(os.path.dirname(__file__) + '/' + module + '.py') as mod:
        data = mod.read()
        matchObj = re.search(r'^(\S*) = Module\(.*', data,
                             re.UNICODE | re.MULTILINE)
        if matchObj:
            name = matchObj.group(1)
            locals()[name] = __import__('station_data.modules.' + module,
                                        globals(), locals(), [name])
            locals()[name] = getattr(locals()[name], name)
