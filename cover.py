"""Support for NeoSmartBlinds covers."""
import logging
from homeassistant.components.cover import CoverDevice, PLATFORM_SCHEMA
from custom_components.neosmartblinds.neosmartblinds.neo_smart_blinds_remote import NeoSmartBlinds
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.script import Script

from homeassistant.components.cover import (
    SUPPORT_CLOSE,
    SUPPORT_OPEN,
    SUPPORT_STOP,
    SUPPORT_SET_POSITION,    
    SUPPORT_OPEN_TILT,
    SUPPORT_CLOSE_TILT,
    CoverDevice,
    
)

from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
)

_LOGGER = logging.getLogger(__name__)

from homeassistant.const import (
    CONF_HOST,
    CONF_NAME,
)

CONF_DEVICE = "blind_code"
CONF_CLOSE_TIME = "close_time"
LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_NAME): cv.string,
        vol.Required(CONF_DEVICE): cv.string,
        vol.Required(CONF_CLOSE_TIME): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up NeoSmartBlinds cover."""
    cover = NeoSmartBlindsCover(
        hass,
        config.get(CONF_NAME),
        config.get(CONF_HOST),
        config.get(CONF_DEVICE),
        config.get(CONF_CLOSE_TIME),
        )
    add_entities([cover])


class NeoSmartBlindsCover(CoverDevice):
    """Representation of a NeoSmartBlinds cover."""

    def __init__(self, hass, name, host, device, close_time):
        """Initialize the cover."""
        self.hass = hass
        self._name = name
        self._host = host
        self._device = device
        self._client = NeoSmartBlinds(host,device, close_time)

    @property
    def name(self):
        """Return the name of the NeoSmartBlinds device."""
        return self._name

    @property
    def should_poll(self):
        """No polling needed within NeoSmartBlinds."""
        return False

    @property
    def supported_features(self):
        """Flag supported features."""
        return SUPPORT_OPEN | SUPPORT_CLOSE | SUPPORT_SET_POSITION | SUPPORT_OPEN_TILT | SUPPORT_CLOSE_TILT | SUPPORT_STOP 

    @property
    def current_cover_position(self):
        """Return the current position of the cover."""
        return 100

    @property
    def device_class(self):
        """Define this cover as either window/blind/awning/shutter."""
        return "blind"
        
    @property
    def is_closed(self):
        """Return if the cover is closed."""
        return None

    @property
    def current_cover_position(self):
        """Return current position of cover."""
        return 50

    @property
    def current_cover_tilt_position(self):
        """Return current position of cover tilt."""
        return 50

    def close_cover(self, **kwargs):
        self._client.sendCommand('dn')
        """Close the cover."""

    def open_cover(self, **kwargs):
        self._client.sendCommand('up')
        """Open the cover."""

    def stop_cover(self, **kwargs):
        self._client.sendCommand('sp')
        """Stop the cover."""
        
    def open_cover_tilt(self, **kwargs):
        self._client.sendCommand('mu')
        """Open the cover tilt."""
        
    def close_cover_tilt(self, **kwargs):
        self._client.sendCommand('md')
        """Close the cover tilt."""

    def set_cover_position(self, **kwargs):
        self._client.adjust(kwargs['position'])
        """Move the cover to a specific position."""

