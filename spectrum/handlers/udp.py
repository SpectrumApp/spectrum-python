import json
import multiprocessing
import socket
import uuid

from spectrum.handlers.base import BaseSpectrumHandler


cpus = multiprocessing.cpu_count()


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
        self.sock.connect((self.UDP_IP, self.UDP_PORT))

        self.sublevel = sublevel

        if self.sublevel is None:
            self.sublevel = 'None'

        super(UDPSpectrum, self).__init__(sublevel, *args, **kwargs)

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
            self.post(message)

    def post(self, message):
        self.sock.sendall(json.dumps(message))
