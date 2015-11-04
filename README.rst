spectrum-python
---------------

::

    $ pip install spectrum-python

Django
======

To direct all logging from your django project to Spectrum, you can use the
predefined `FIRE_HOSE` logging configuration::

    # settings.py

    from spectrum.django import spectrum
    LOGGING = spectrum.FIRE_HOSE
