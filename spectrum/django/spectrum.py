FIRE_HOSE = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'root']
    },
    'filters': {
        'request_id': {
            '()': 'spectrum.filters.RequestIdFilter'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(name)s][%(levelname)s] %(message)s'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['django.request'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['django.db.backends'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['request_id']
        },
        'root': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.RestSpectrum',
            'sublevel': '',
            'filters': ['request_id']
        },
        'django': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.RestSpectrum',
            'sublevel': 'django',
            'filters': ['request_id']
        },
        'django.request': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.RestSpectrum',
            'sublevel': 'django.request',
            'filters': ['request_id']
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.RestSpectrum',
            'sublevel': 'celery',
            'filters': ['request_id']
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.RestSpectrum',
            'sublevel': 'django.db.backends',
        },
    },
}

FIRE_HOSE_UDP = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'root']
    },
    'filters': {
        'request_id': {
            '()': 'spectrum.filters.RequestIdFilter'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(name)s][%(levelname)s] %(message)s'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['django.request'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['django.db.backends'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['request_id']
        },
        'root': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.UDPSpectrum',
            'sublevel': '',
        },
        'django': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.UDPSpectrum',
            'sublevel': 'django',
        },
        'django.request': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.UDPSpectrum',
            'sublevel': 'django.request',
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.UDPSpectrum',
            'sublevel': 'celery',
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.UDPSpectrum',
            'sublevel': 'django.db.backends',
        },
    },
}

FIRE_HOSE_WS = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'root']
    },
    'filters': {
        'request_id': {
            '()': 'spectrum.filters.RequestIdFilter'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[%(name)s][%(levelname)s] %(message)s'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['django.request'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['django.db.backends'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['request_id']
        },
        'root': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.WebsocketSpectrum',
            'sublevel': '',
        },
        'django': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.WebsocketSpectrum',
            'sublevel': 'django',
        },
        'django.request': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.WebsocketSpectrum',
            'sublevel': 'django.request',
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.WebsocketSpectrum',
            'sublevel': 'celery',
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.WebsocketSpectrum',
            'sublevel': 'django.db.backends',
        },
    },
}

def fire_hose(base_config=None, log_db=True, levels=None, handler_kwargs=None):
    """

    A convenience method to get and modify predefined logging configurations.

    Arguments
    ~~~~~~~~~

    * ``base_config``: Defaults to `FIRE_HOSE`, which uses the REST HTTP stream on ``http://127.0.0.1:9000/``
    * ``log_db``: shortcut for toggling the level of ``django.db.backends`` logging. Defaults to ``True``
    * ``levels``: if provided, a 2-tuples iterable of logger names and their level.
    * ``handler_kwargs``: if provided, kwargs to pass to the handles. Use this to override default settings such as ip / port Spectrum is running on.

    Examples
    ~~~~~~~~

    ::

        from spectrum.django import fire_hose, FIRE_HOSE_UDP


        LOGGING = fire_hose()

        LOGGING = fire_hose(log_db=False)

        LOGGING = fire_hose(levels=(
            ('my.overly.verbose.module', 'WARNING'),
            ('some.other.module', 'CRITICAL'),
        )

        LOGGING = fire_hose(FIRE_HOSE_UDP, handler_kwargs={'url': '127.0.0.1:12345'})

    """

    if base_config is None:
        base_config = FIRE_HOSE

    if levels is None:
        levels = tuple()

    if handler_kwargs is None:
        handler_kwargs = {}

    if log_db is False:
        base_config['loggers']['django.db.backends']['level'] = 'WARNING'

    for silenced, level in levels:
        if silenced not in base_config['loggers']:
            base_config['loggers'][silenced] = {}

        base_config['loggers'][silenced]['level'] = level

    for handler, handler_config in base_config['handlers'].items():
        handler_config.update(handler_kwargs)

    return base_config
