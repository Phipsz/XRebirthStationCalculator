import multiprocessing
import logging
import locale

from x_rebirth_station_calculator.web.translations import LANGLIST

try:
    from gunicorn.app.base import BaseApplication as GunicornBaseApplication
    from gunicorn.six import iteritems
except:
    GunicornBaseApplication = type
    iteritems = None


HANDLERS = {
    '': 'handler_station_calc',
    'station_calc': 'handler_calculate_wares',
    'stations': 'handler_get_station_info',
    'wares': 'handler_calculate_wares',
    'static': 'handler_staticfiles',
}

ENABLE_STATICFILES = False
PREFIX = ''
_log = logging.getLogger('XRStationCalc.http_control')


def number_of_workers():
    """ Get number of maximum workers. """
    return (multiprocessing.cpu_count() * 2) + 1


def handler_main(environ, start_response):
    """ Wsgi entry point. """
    path = environ.get('PATH_INFO')
    prefix, _, suffix = path[1:].partition('/')
    if prefix in LANGLIST:
        environ['LANGUAGE'] = prefix
        prefix, _, suffix = suffix.partition('/')

    handler = eval(HANDLERS.get(prefix, 'handler_404'))
    _log.debug('Received request for prefix %s' % (prefix, ))

    status, response_headers, response_body = handler(environ, suffix)

    start_response(status, response_headers)

    return [response_body]


def handler_station_calc(environ, suffix=None):
    from x_rebirth_station_calculator import station_data
    from operator import methodcaller
    import urllib
    import re
    language = environ.get('LANGUAGE', 'L044')
    amounts = None
    selections = None
    if environ['REQUEST_METHOD'] == 'GET':
        amounts = dict()
        selections = dict()
        params = urllib.parse.parse_qs(environ.get('QUERY_STRING'))
        for key in sorted(params.keys()):
            match_obj = re.match(r'station-([0-9]+)', key)
            if match_obj:
                selections[int(match_obj.group(1))] = params[key][0]
            match_obj = re.match(r'c-station-([0-9]+)', key)
            if match_obj:
                amounts[int(match_obj.group(1))] = int(params[key][0])
    if not language:
        language = 'L044'
    station_list = list(station_data.station_list)
    empty_station = station_data.station_base.Station({'L044': '------'}, [])
    station_list.insert(0, empty_station)
    _log.debug('Selected language: ' + str(language))
    if language:
        station_list.sort(key=methodcaller('get_name', language))
    else:
        station_list.sort(key=methodcaller('get_name'))
    status = '200 OK'
    template = _load_template('calculator.html')
    response_body = _render_template(template,
                                     title=LANGLIST[language]['subtitle'],
                                     station_list=station_list,
                                     language=language,
                                     num_inputs=len(selections) + 10,
                                     translations=LANGLIST[language],
                                     langlist=sorted(LANGLIST.keys()),
                                     amounts=amounts, selections=selections,
                                     station_intern=station_data.name_mappings)
    response_headers = [
        ('Content-Type', 'text/html; charset=UTF-8'),
    ]
    return status, response_headers, response_body


def handler_calculate_wares(environ, suffix=None):
    from x_rebirth_station_calculator import station_data
    from x_rebirth_station_calculator.web.translations import LOCALE_LIST
    from operator import methodcaller
    from decimal import Decimal
    import urllib
    import re
    print(environ)
    if environ['REQUEST_METHOD'] != 'GET':
        return handler_404(environ)
    language = environ.get('LANGUAGE', 'L044')
    if not language:
        language = 'L044'
    locale.setlocale(locale.LC_ALL, LOCALE_LIST[language])
    amounts = dict()
    selections = dict()
    params = urllib.parse.parse_qs(environ.get('QUERY_STRING'))
    for key in sorted(params.keys()):
        match_obj = re.match(r'station-([0-9]+)', key)
        if match_obj:
            selections[int(match_obj.group(1))] = params[key][0]
        match_obj = re.match(r'c-station-([0-9]+)', key)
        if match_obj:
            amounts[int(match_obj.group(1))] = int(params[key][0])

    wares = {'productions': dict(),
             'consumptions': dict(),
             'result': dict(),
             'list': set()}
    for i in sorted(selections.keys()):
        station = getattr(station_data, selections[i])
        count = Decimal(amounts[i])
        productions = station.get_production_data()
        consumptions = station.get_consumption_data()
        for prdctn in productions:
            warename = prdctn.ware.get_name()
            wares['list'].add(prdctn.ware)
            rate = prdctn.get_production_rate() * count
            if warename in wares['productions']:
                wares['productions'][warename] += rate
            else:
                wares['productions'][warename] = rate
        for cnsmptn in consumptions:
            warename = cnsmptn.ware.get_name()
            wares['list'].add(cnsmptn.ware)
            rate = cnsmptn.get_consumption_rate() * count
            if warename in wares['consumptions']:
                wares['consumptions'][warename] += rate
            else:
                wares['consumptions'][warename] = rate
    wares['list'] = sorted(wares['list'], key=methodcaller('get_name'))
    for ware in wares['list']:
        prod_rate = wares['productions'].get(ware.get_name(), 0)
        cons_rate = wares['consumptions'].get(ware.get_name(), 0)
        result = prod_rate - cons_rate
        wares['result'][ware.get_name()] = result.quantize(Decimal('0.01'))

    status = '200 OK'
    template = _load_template('wares.html')
    response_body = _render_template(template,
                                     wares=wares,
                                     language=language,
                                     translations=LANGLIST[language],
                                     formatter=formatter(language))
    response_headers = [
        ('Content-Type', 'text/html; charset=UTF-8'),
    ]
    return status, response_headers, response_body


def handler_get_station_info(environ, suffix=None):
    from x_rebirth_station_calculator import station_data
    from x_rebirth_station_calculator.web.translations import LOCALE_LIST

    try:
        station = getattr(station_data, suffix)
    except AttributeError:
        return handler_404(environ)
    language = environ.get('LANGUAGE', 'L044')
    if not language:
        language = 'L044'
    locale.setlocale(locale.LC_ALL, LOCALE_LIST[language])
    status = '200 OK'
    template = _load_template('station.html')
    response_body = _render_template(template, station=station,
                                     translations=LANGLIST[language],
                                     language=language,
                                     title=LANGLIST[language]['station_info'],
                                     formatter=formatter(language))

    response_headers = [
        ('Content-Type', 'text/html; charset=UTF-8'),
    ]
    return status, response_headers, response_body


def handler_404(environ, suffix=None):
    """ Generate 404 webpage. """
    status = '404 Not Found'
    template = _load_template('404.html')
    response_body = _render_template(template, title='404')
    response_headers = [
        ('Content-Type', 'text/html; charset=UTF-8'),
    ]
    return status, response_headers, response_body


def formatter(language):
    from x_rebirth_station_calculator.web.translations import LOCALE_LIST
    locale.setlocale(locale.LC_ALL, LOCALE_LIST[language])

    def func(data):
        return locale.format('%.2f', data, grouping=True)
    return func


def handler_staticfiles(environ, path):
    """ Return static file.

    Should only be used in development code. In production environments the
    static files should be served by the webserver.
    """
    if not ENABLE_STATICFILES:
        return handler_404(environ)
    import os
    import mimetypes
    file_path = os.path.dirname(__file__) + '/../../share/static/' + path
    _log.debug('staticfiles searching %s' % file_path)
    if not os.path.exists(file_path):
        return handler_404(environ)
    status = '200 OK'
    file_type = mimetypes.guess_type(file_path)[0]
    if not file_type:
        file_type = 'text/plain'
    response_headers = [
        ('Content-Type', file_type),
    ]
    response_body = b''
    with open(file_path, 'rb') as static_file:
        response_body = static_file.read()
    return status, response_headers, response_body


def _load_template(template_name):
    import os
    import jinja2
    _log.debug(os.path.dirname(__file__))
    loader = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader('/usr/local/share/XRebirthStationCalculator'),
        jinja2.FileSystemLoader(os.path.dirname(__file__) + '/../../share'),
    ])
    env = jinja2.Environment(loader=loader)
    template = env.get_template(template_name,
                                globals={'prefix': PREFIX,
                                         'isinstance': isinstance,
                                         'tuple': tuple})
    return template


def _render_template(template, **kwargs):
    rendered = template.render(**kwargs)
    return rendered.encode('utf-8')


class WebApplication(GunicornBaseApplication):

    def __init__(self, app, options=None):
        self.options = options
        self.application = app
        super().__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def setup_env(application_prefix=None):
    """ Setup the environent, so everything is ready to be served.

    Here you can set the two basic of the wsgi application, of which the server
    needs to be aware of.
    """
    global PREFIX

    if application_prefix is None:
        PREFIX = '/'
    else:
        PREFIX = application_prefix
        if not PREFIX.startswith('/'):
            PREFIX = '/' + PREFIX
        if not PREFIX.endswith('/'):
            PREFIX = PREFIX + '/'


def run():
    """ Start gunicorn server for development. """
    import argparse
    global ENABLE_STATICFILES
    global PREFIX
    parser = argparse.ArgumentParser()
    parser.add_argument('--enable-static-files', action='store_true',
                        help='''Static files are served by this program. This
                        is only being encouraged for development''')
    parser.add_argument('-p', '--port', default='8010',
                        help='''Define the port on which to receive requests.
                        Defaults to 8010''')
    parser.add_argument('--prefix', default='/', help='''The prefix the
                        application should use. Defaults to '/' ''')
    parser.add_argument('-v', action='count', default=0)

    args = parser.parse_args()
    logging.basicConfig(level=50 - (args.v * 10))
    ENABLE_STATICFILES = args.enable_static_files
    _log.debug('Serving staticfiles: ' + str(ENABLE_STATICFILES))

    setup_env(args.prefix)

    options = {
        'bind': '%s:%s' % ('127.0.0.1', args.port),
        'workers': number_of_workers(),
        'timeout': 30,
        'preload_app': True,
    }
    try:
        WebApplication(handler_main, options).run()
    except TypeError:
        print("Gunicorn is needed for running the development server\n"
              "Just run:\n"
              " $ pip install gunicorn")
