import datetime
import logging
import traceback
import uuid


class BaseSpectrumHandler(logging.Handler):
    def __init__(self, sublevel=None, *args, **kwargs):
        self.sublevel = sublevel

        super(BaseSpectrumHandler, self).__init__(*args, **kwargs)

    def get_sub_level(self, record):
        if self.sublevel is not None:
            return self.sublevel
        else:
            return record.name

    def build_message(self, record):
        return {
            'id': uuid.uuid1().hex,
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
