import datetime
import json
import logging
import socket
import time
import traceback
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
import uuid

from requests_futures.sessions import FuturesSession
from .silent import SilentExecutor

from ..conf import SPECTRUM_UUID4

session = FuturesSession(executor=SilentExecutor(max_workers=2))


socket.setdefaulttimeout(0.1)


def cb(sess, resp):
    """ Do not thing with the callback """
    pass


class BaseSpectrumHandler(logging.Handler):

    def __init__(self, sublevel=None, *args, **kwargs):
        """ Setup """
        self.url = kwargs.pop('url', 'http://127.0.0.1:9000/?spectrum=%s' % SPECTRUM_UUID4)

        self.conn_info = urlparse(self.url)
        self.sublevel = sublevel

        if self.sublevel is None:
            self.sublevel = 'None'

        self.headers = {'content-type': 'application/json'}

        self._last_checked = time.time()
        self._is_port_open = None

        super(BaseSpectrumHandler, self).__init__(*args, **kwargs)

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

    def get_sub_level(self, record):
        return self.sublevel

    def emit(self, record):
        """
        Actually send the record to Spectrum over the REST interface
        """

        if not self.is_port_open(self.conn_info.hostname, self.conn_info.port):
            return

        try:
            data = {
                'id': str(uuid.uuid4().hex),
                'timestamp': str(datetime.datetime.now()),
                'level': record.levelname,
                'sublevel': self.get_sub_level(record),
                'message': record.getMessage(),
                'filename': record.filename,
                'path': record.pathname,
                'line': record.lineno,
                'process_name': record.processName,
                'process': record.process,
                'function': record.funcName,
                'traceback': traceback.format_exception(*record.exc_info) if record.exc_info else None,
            }
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


class Spectrum(BaseSpectrumHandler):
    pass
