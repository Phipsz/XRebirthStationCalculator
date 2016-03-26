""" The wsgi module can be used to serve the application by apaches mod_wsgi.

This module needs to be the only module in the web package. For more detailed
information take a look in the __init__.
"""

from x_rebirth_station_calculator.web import http_control
import logging
import logging.handlers


def application(environ, start_response):
    """ Wsgi function for apache.

    The application can be changed in behaviour by the following enviromental
    variables:
        * XREBIRTHSTATIONCALC_DEBUG:
            If set to 1 debug messages are written to syslog
        * XREBIRTHSTATIONCALC_PREFIX:
            If set the application runs under a subfolder described in prefix.

    These variables are not part of the system environment! They are part of
    the `environ` parameter which can be modified within apache with `SetEnv`.
    """
    log = logging.getLogger('XRStationCalc')
    syslog = logging.handlers.SysLogHandler(address='/dev/log')
    formatter = logging.Formatter('%(module)s: %(message)s')

    if environ.get('XREBIRTHSTATIONCALC_DEBUG', '0') == '1':
        log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
    else:
        log.setLevel(logging.INFO)

    syslog.setFormatter(formatter)
    log.addHandler(syslog)

    log.debug('Got environment from apache: %s' % environ)

    http_control.setup_env(
        environ.get('XREBIRTHSTATIONCALC_PREFIX', None),
    )
    return http_control.handler_main(environ, start_response)
