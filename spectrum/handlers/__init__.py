from .rest import RestSpectrum
from .rest import RestSpectrum as Spectrum
from .udp import UDPSpectrum

try:
    from .websocket import WebsocketSpectrum
except ImportError:
    WebsocketSpectrum = None
