import json
import multiprocessing
import socket
import time
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from spectrum.conf import SPECTRUM_UUID4

from requests_futures.sessions import FuturesSession

from .base import BaseSpectrumHandler
from .silent import SilentExecutor


socket.setdefaulttimeout(0.1)

cpus = multiprocessing.cpu_count()
session = FuturesSession(executor=SilentExecutor(max_workers=cpus))


def cb(sess, resp):
    """ Do not thing with the callback """
    pass


class RestSpectrum(BaseSpectrumHandler):

    def __init__(self, sublevel=None, *args, **kwargs):
        """ Setup """
        url = kwargs.pop('url', 'http://127.0.0.1:9000/')

        self.url = '%s?spectrum=%s' % (url, SPECTRUM_UUID4)

        self.conn_info = urlparse(self.url)
        self.headers = {'content-type': 'application/json'}

        self._last_checked = time.time()
        self._is_port_open = None

        super(RestSpectrum, self).__init__(sublevel, *args, **kwargs)

    def check_port(self, hostname, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostname, port))
        return result == 0

    def is_port_open(self, hostname, port):
        expired = (time.time() - self._last_checked) > 60
        if expired or self._is_port_open is None:
            self._is_port_open = self.check_port(hostname, port)
            self._last_checked = time.time()

        return self._is_port_open

    def emit(self, record):
        """
        Actually send the record to Spectrum over the REST interface
        """

        if not self.is_port_open(self.conn_info.hostname, self.conn_info.port):
            return

        try:
            data = self.build_message(record)

            session.post(
                self.url,
                data=json.dumps(data),
                headers=self.headers,
                background_callback=cb
            )

        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
