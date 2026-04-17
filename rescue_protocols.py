import urllib3
import ssl
from typing import Any, Dict

class APIRescueProtocol:
    """
    Implements fail-safes for brittle production APIs.
    Based on real-world resolutions for SSLV3 and Schema Desyncs.
    """

    @staticmethod
    def create_legacy_session():
        """
        Bypasses SSLV3_ALERT_HANDSHAKE_FAILURE on modern Python (3.12+)
        by injecting legacy cipher overrides into the transport layer.
        """
        # RADAR Mapping: Capability to maintain uptime in legacy environments.
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT@SECLEVEL=1') # Lowering security level for legacy compatibility
        
        http = urllib3.PoolManager(ssl_context=context)
        return http

    @staticmethod
    def type_agnostic_parser(raw_response: Dict[str, Any], key: str) -> float:
        """
        Rescues data from 'Ghost Settlement' or schema shifts where 
        integers, strings, and floats are mixed inconsistently by the API.
        """
        value = raw_response.get(key, 0)
        try:
            # Force normalization to float regardless of incoming type
            return float(str(value).replace('$', '').replace(',', ''))
        except (ValueError, TypeError):
            # Fallback to 0.0 or a 'Sentinel Value' to prevent pipeline crash
            return 0.0
