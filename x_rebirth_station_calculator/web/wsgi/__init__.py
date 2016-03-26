""" This module protects the sources from misconfigured webservers.

The wsgi module in here is loaded by a webserver, so the server needs access.
To protect the administration from accidential file serving of the whole
module, this module has been created.
"""
