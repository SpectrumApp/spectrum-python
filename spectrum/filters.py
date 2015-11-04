import logging


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        return "POST /?spectrum" not in record.msg
