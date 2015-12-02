import datetime
import json
import logging
import multiprocessing
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

cpus = multiprocessing.cpu_count()
session = FuturesSession(executor=SilentExecutor(max_workers=cpus))


socket.setdefaulttimeout(0.1)


def cb(sess, resp):
    """ Do not thing with the callback """
    pass


class BaseSpectrumHandler(logging.Handler):
    def __init__(self, sublevel=None, *args, **kwargs):
        self.sublevel = sublevel

        if self.sublevel is None:
            self.sublevel = 'None'

        super(BaseSpectrumHandler, self).__init__(*args, **kwargs)

    def get_sub_level(self, record):
        return self.sublevel

    def build_message(self, record):
        return {
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


class Spectrum(BaseSpectrumHandler):

    def __init__(self, sublevel=None, *args, **kwargs):
        """ Setup """
        self.url = kwargs.pop('url', 'http://127.0.0.1:9000/?spectrum=%s' % SPECTRUM_UUID4)

        self.conn_info = urlparse(self.url)
        self.headers = {'content-type': 'application/json'}

        self._last_checked = time.time()
        self._is_port_open = None

        super(Spectrum, self).__init__(*args, **kwargs)

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


class UDPSpectrum(BaseSpectrumHandler):

    MAX_LENGTH = 64 * 1024

    preamble = json.dumps({
        "index": 0,
        "total": 1,
        'id': str(uuid.uuid4().hex),
    })

    MAX_DATA_LENGTH = MAX_LENGTH - len(preamble)

    def __init__(self, sublevel=None, *args, **kwargs):
        """ Setup """
        self.url = kwargs.pop('url', '127.0.0.1:55933')
        self.UDP_IP, self.UDP_PORT = self.url.split(':')
        self.UDP_PORT = int(self.UDP_PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.sublevel = sublevel

        if self.sublevel is None:
            self.sublevel = 'None'

        super(UDPSpectrum, self).__init__(*args, **kwargs)

    def emit(self, record):

        data = json.dumps(self.build_message(record))
        id = str(uuid.uuid4().hex)

        chunks = []
        offset = 0
        while offset < len(data):
            chunks.append(
                data[offset:self.MAX_DATA_LENGTH]
            )
            offset += self.MAX_DATA_LENGTH

        total = len(chunks)
        for i, chunk in enumerate(chunks):
            message = {
                "id": id,
                "index": i,
                "total": total,
                "data": chunk,
            }
            self.sock.sendto(json.dumps(message), (self.UDP_IP, self.UDP_PORT))
