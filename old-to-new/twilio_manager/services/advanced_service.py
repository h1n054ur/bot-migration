from twilio.rest import Client
from twilio_manager.shared.config import ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def configure_app_api(config_params: dict) -> tuple[bool, str | None]:
    """Configure application with given parameters.
    
    Args:
        config_params (dict): Configuration parameters
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        # Validate required parameters
        if not isinstance(config_params, dict):
            return False, "Configuration must be a dictionary"
            
        # Apply configuration
        for key, value in config_params.items():
            # Here we would persist the configuration
            # For now, just validate the key/value pairs
            if not isinstance(key, str):
                return False, f"Invalid configuration key: {key}"
            if not isinstance(value, (str, int, float, bool, list, dict)):
                return False, f"Invalid configuration value type for {key}"
                
        return True, None
    except Exception as e:
        return False, str(e)

def search_api(query: str) -> tuple[list, str | None]:
    """Search Twilio resources based on query string.
    
    Args:
        query (str): Search query
        
    Returns:
        tuple[list, str | None]: (results_list, error_message)
    """
    try:
        results = []
        query = query.lower().strip()
        
        # Search phone numbers
        try:
            numbers = client.incoming_phone_numbers.list()
            for num in numbers:
                if (query in num.phone_number.lower() or 
                    query in (num.friendly_name or "").lower()):
                    results.append({
                        "type": "phone_number",
                        "sid": num.sid,
                        "value": num.phone_number,
                        "name": num.friendly_name
                    })
        except Exception:
            pass
            
        # Search applications
        try:
            apps = client.applications.list()
            for app in apps:
                if query in (app.friendly_name or "").lower():
                    results.append({
                        "type": "application",
                        "sid": app.sid,
                        "value": app.voice_url,
                        "name": app.friendly_name
                    })
        except Exception:
            pass
            
        # Search SIP trunks
        try:
            trunks = client.trunking.v1.trunks.list()
            for trunk in trunks:
                if query in (trunk.friendly_name or "").lower():
                    results.append({
                        "type": "sip_trunk",
                        "sid": trunk.sid,
                        "value": trunk.voice_region,
                        "name": trunk.friendly_name
                    })
        except Exception:
            pass
            
        return results, None
    except Exception as e:
        return [], str(e)
