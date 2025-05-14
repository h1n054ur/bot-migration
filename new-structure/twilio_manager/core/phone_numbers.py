from twilio_manager.services.phone_service import (
    search_available_numbers_api,
    purchase_number_api,
    configure_number_api,
    release_number_api
)

def search_available_numbers(country_code, number_type="local", capabilities=None, pattern=""):
    """
    Search for available phone numbers via Twilio API.
    """
    return search_available_numbers_api(country_code, number_type, capabilities, pattern)

def purchase_number(phone_number: str):
    """
    Purchase a phone number via Twilio API.
    """
    return purchase_number_api(phone_number)

def configure_number(phone_number: str, config_params: dict):
    """
    Configure a purchased phone number via Twilio API.
    """
    return configure_number_api(phone_number, config_params)

def release_number(phone_number: str):
    """
    Release a purchased phone number via Twilio API.
    """
    return release_number_api(phone_number)
