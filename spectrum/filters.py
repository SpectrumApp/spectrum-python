import logging

from .conf import SPECTRUM_UUID4


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        return "POST /?spectrum=%s" % SPECTRUM_UUID4 not in record.msg
