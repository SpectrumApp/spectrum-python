spectrum-python
---------------

::

    $ pip install spectrum-python

Django
======

To direct all logging from your Django project to Spectrum, you can use the
predefined `FIRE_HOSE` logging configuration::

    # settings.py

    from spectrum.django import spectrum
    LOGGING = spectrum.FIRE_HOSE

If you use `celery`, you'll have one more setting to add::

    CELERYD_HIJACK_ROOT_LOGGER = False
