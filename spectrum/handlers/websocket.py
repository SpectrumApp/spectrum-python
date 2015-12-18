import json
import multiprocessing
import threading
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from spectrum.conf import SPECTRUM_UUID4

from spectrum.handlers.base import BaseSpectrumHandler
from autobahn.asyncio.websocket import WebSocketClientProtocol
from autobahn.asyncio.websocket import WebSocketClientFactory

try:
    import asyncio
except ImportError:
    # Trollius >= 0.3 was renamed
    import trollius as asyncio

queue = multiprocessing.Queue()
loop = asyncio.get_event_loop()

factory = WebSocketClientFactory()


def listener(queue, proto):
    while proto.connected:
        message = queue.get()
        if message is not None:
            proto.sendMessage(message, isBinary=False)


class SpectrumProtocol(WebSocketClientProtocol):
    def onOpen(self):
        self.listener = multiprocessing.Process(target=listener, args=(queue, self,))
        self.listener.start()
        self.listener.join()

    def onConnect(self, response):
        self.connected = True
        print("Connected to Server: {}".format(response.peer))

    def onClose(self):
        self.connected = False


def worker(loop, hostname, port):
    factory.protocol = SpectrumProtocol
    asyncio.set_event_loop(loop)
    coro = loop.create_connection(factory, hostname, port)
    try:
        loop.run_until_complete(coro)
        loop.close()
    except RuntimeError:
        pass


class WebsocketSpectrum(BaseSpectrumHandler):
    def __init__(self, sublevel=None, *args, **kwargs):
        """ Setup """
        self.url = kwargs.pop('url', 'ws://127.0.0.1:9200/?spectrum=%s' % SPECTRUM_UUID4)
        self.conn_info = urlparse(self.url)
        self.start(self.conn_info.hostname, self.conn_info.port)
        super(WebsocketSpectrum, self).__init__(sublevel, *args, **kwargs)

    def emit(self, record):
        data = self.build_message(record)
        payload = json.dumps(data, ensure_ascii=False).encode('utf8')
        queue.put(payload)

    def start(cls, hostname, port):
        try:
            t = threading.Thread(target=worker, args=(loop, hostname, port,))
            t.start()
        except RuntimeError:
            pass
