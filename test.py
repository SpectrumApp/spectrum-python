import logging
from spectrum.handlers import Spectrum, SpectrumModules

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#spectrum = Spectrum('my-sub-level')
#logger.addHandler(spectrum)

spectrum = SpectrumModules(levels=3)
logger.addHandler(spectrum)

for i in range(5):
    logger.info("informational blah")
    logger.warn("warning blah")
    logger.debug("debugging blah")
