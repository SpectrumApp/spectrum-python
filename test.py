import logging
from spectrum.handlers import Spectrum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

spectrum = Spectrum('my-sub-level')
logger.addHandler(spectrum)

logger.info("informational blah")
logger.warn("warning blah")
logger.debug("debugging blah")
