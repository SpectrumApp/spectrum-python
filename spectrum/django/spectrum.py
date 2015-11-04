FIRE_HOSE = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'spectrum']
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
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['request_id']
        },
        'spectrum': {
            'level': 'DEBUG',
            'class': 'spectrum.handlers.Spectrum',
            'sublevel': 'django',
            'filters': ['request_id']
        },
    },
}
