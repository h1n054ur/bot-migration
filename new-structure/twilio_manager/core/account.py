from twilio_manager.services.account_service import (
    get_account_info_api,
    list_api_keys_api,
    list_subaccounts_api,
    list_sip_trunks_api,
    list_twiml_apps_api
)

def get_account_info():
    """
    Retrieve account information via Twilio API.
    """
    return get_account_info_api()

def list_api_keys():
    """
    Retrieve API Keys via Twilio API.
    """
    return list_api_keys_api()

def list_subaccounts():
    """
    Retrieve subaccounts via Twilio API.
    """
    return list_subaccounts_api()

def list_sip_trunks():
    """
    Retrieve SIP Trunks via Twilio API.
    """
    return list_sip_trunks_api()

def list_twiml_apps():
    """
    Retrieve TwiML Apps via Twilio API.
    """
    return list_twiml_apps_api()
