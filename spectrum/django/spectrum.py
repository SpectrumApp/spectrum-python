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
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': '',
            'filters': ['request_id']
        },
        'django': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': 'django',
            'filters': ['request_id']
        },
        'django.request': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': 'django.request',
            'filters': ['request_id']
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': 'celery',
            'filters': ['request_id']
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': 'django.db.backends',
            'filters': ['request_id']
        },
    },
}
