from twilio_manager.services.voice_service import (
    make_call_api,
    get_conferences_api,
    get_recordings_api,
    get_call_logs_api
)

def make_call(to_number: str, from_number: str, url: str):
    """
    Make a voice call via Twilio API.
    """
    return make_call_api(to_number, from_number, url)

def get_conferences(limit: int = 50):
    """
    Retrieve active conferences via Twilio API.
    """
    return get_conferences_api(limit)

def get_recordings(limit: int = 50):
    """
    Retrieve call recordings via Twilio API.
    """
    return get_recordings_api(limit)

def get_call_logs(limit: int = 50):
    """
    Retrieve call logs via Twilio API.
    """
    return get_call_logs_api(limit)
