import datetime
import json
import logging
import uuid

from requests_futures.sessions import FuturesSession

session = FuturesSession()


def cb(sess, resp):
    """ Do not thing with the callback """
    pass


class BaseSpectrumHandler(logging.Handler):

    def __init__(self, sublevel=None, url='http://127.0.0.1:9000'):
        """ Setup """
        super(BaseSpectrumHandler, self).__init__()
        self.url = url
        self.sublevel = sublevel
        self.headers = {'content-type': 'application/json'}

    def get_sub_level(self, record):
        return self.sublevel

    def emit(self, record):
        """
        Actually send the record to Spectrum over the REST interface
        """
        try:
            data = {
                'id': str(uuid.uuid4().hex),
                'timestamp': str(datetime.datetime.now()),
                'level': record.levelname,
                'sublevel': self.get_sub_level(record),
                'message': record.getMessage(),
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
