X Rebirth Station Calculator
============================

This Software can be used to calculate ware consumption and production for
Station Complexes built in the game X:Rebirth.

Prerequisites
-------------

Uses Twitter-Bootstrap for the webfrontend. (published under MIT License. Get
it at https://getbootstrap.com/ .

Needs python3, python3-setuptools, python3-pbr.


Installation
------------

First, you need to install all files. run

.. code-block:: bash

    # python3 setup.py install

You have now installed all needed files, except specific configuration needed
for the webserver.

Apache2 (untested)

    You will need *mod_wsgi* to be able to use the shipped configuration.
    Install and enable it first. Copy *etc/apache/xrebirthstationcalc.conf* to
    */etc/apache2/conf-available*. Now you can enable it, for example using
    *a2enconf* on debian-based distros. After reloading apache, the website
    will be served at *hostname*/xrstcalc.

    **Note**: The config file expects the wsgi.py to be at
    */usr/local/lib/python3.4/dist-packages/x_rebirth_station_calculator/web/wsgi/wsgi.py*.
    If you used a custom install path or are using a different version of
    Python3, this path needs to be adjusted!

LightTPD

    Requires the wsgi-server gunicorn. Configuration not yet documented.


Nginx

    I have not found a way to use a wsgi application with nginx yet. If you
    know a working configuration, please share to update this Readme.
