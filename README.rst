===============
spectrum-python
===============

Overview
========

`Spectrum <http://www.devspectrum.com>`_ is a application that helps
developers filter and sift through logs while developing or debugging
locally. It accepts logging information via a REST API, syslog, or can be
set to tail local files.  All of these logging sources are then easily
shown or hidden depending on the current needs of the developer.

This Python package makes it trivially easy to push logs from Python and/or Django into Spectrum.

Python
======

Installing Python support for Spectrum is as easy as::

    $ pip install spectrum-python

Setting up a logging handler is also equally easy::

    import logging
    from spectrum.handlers import Spectrum

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    spectrum = Spectrum('my-logging-sublevel')
    logger.addHandler(spectrum)

    for i in range(5):
        logger.info("This would be sent as INFO.my-logging-sublevel")
        logger.warn("This would be sent as WARNING.my-logging-sublevel")
        logger.debug("This would be sent as DEBUG.my-logging-sublevel")


Django
======

To direct all logging from your Django project to Spectrum, you can use the
predefined `FIRE_HOSE` logging configuration::

    # settings.py

    from spectrum.django import spectrum
    LOGGING = spectrum.FIRE_HOSE

If you use `celery`, you'll have one more setting to add::

    CELERYD_HIJACK_ROOT_LOGGER = False
