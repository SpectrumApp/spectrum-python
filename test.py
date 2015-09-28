import logging
from spectrum.handlers import Spectrum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

spectrum = Spectrum('my-sub-level')
logger.addHandler(spectrum)

for i in range(5):
    logger.info("blah blah informational blah")
    logger.warn("blah blah warning blah")
    logger.debug("blah blah debugging blah")
