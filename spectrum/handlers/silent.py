import logging
from concurrent.futures import ThreadPoolExecutor


class DisableLogger():
    def __init__(self, level):
        self.level = level

    def __enter__(self):
        logging.disable(self.level)

    def __exit__(self, *args, **kwargs):
        logging.disable(logging.NOTSET)


class SilentExecutor(ThreadPoolExecutor):
    def submit(self, func, *args, **kwargs):
        def wrap(*args_, **kwargs_):
            with DisableLogger(logging.INFO):
                func(*args_, **kwargs_)
        return super(SilentExecutor, self).submit(wrap, *args, **kwargs)
