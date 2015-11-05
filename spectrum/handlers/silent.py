import logging
from concurrent.futures import ThreadPoolExecutor


class DisableLogger():
    def __enter__(self):
        logging.shutdown()

    def __exit__(self, *args, **kwargs):
        pass


class SilentExecutor(ThreadPoolExecutor):
    def submit(self, func, *args, **kwargs):
        def wrap(*args_, **kwargs_):
            with DisableLogger():
                func(*args_, **kwargs_)
        return super(SilentExecutor, self).submit(wrap, *args, **kwargs)
