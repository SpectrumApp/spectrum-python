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

Options
-------

url
~~~

IP and PORT of the REST API to use.  Defaults to 'http://0.0.0.0:9000'.  You must override this to the proper Spectrum port associated to your stream if using more than one REST API Stream

sublevel
~~~~~~~~

Optional sub-level to use for this handler.  Defaults to '<untitled>' in the Spectrum UI if not given.


Django
======

To direct all logging from your Django project to Spectrum, you can use the
predefined `FIRE_HOSE` logging configuration in your settings::

    # settings.py

    from spectrum.django import FIRE_HOSE
    LOGGING = FIRE_HOSE

If you use `celery`, you'll have one more setting to add::

    CELERYD_HIJACK_ROOT_LOGGER = False

You can also use the ``fire_hose`` convenience method to quickly modify any of
the pre-built logging configuration dict::

        from spectrum.django import fire_hose


        LOGGING = fire_hose()

        LOGGING = fire_hose(log_db=False)

        LOGGING = fire_hose(levels=(
            ('my.overly.verbose.module', 'WARNING'),
            ('some.other.module', 'CRITICAL'),
        )

        LOGGING = fire_hose(handler_kwargs={'url': '127.0.0.1:12345'})

If you prefer a more granular approach, you can configure specific handlers::

    # settings.py

    LOGGING = {
        ...
        'filters': {
            'request_id': {
                '()': 'spectrum.filters.RequestIdFilter'
            }
        },
        'handlers': {
            'myloggername': {
                'level': 'DEBUG',
                'class': 'spectrum.handlers.RestSpectrum',
                'sublevel': 'myloggername',
                'filters': ['request_id']
            }
        }
    }

Make sure you include the ``request_id`` filter to filter out spectrum's own requests from the other. Otherwise, Spectrum's requests will be logged by Python, and those logs will in turn generate their own Spectrum request, causing and infinite recursion.

