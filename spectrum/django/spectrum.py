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
