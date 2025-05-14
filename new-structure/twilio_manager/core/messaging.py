from twilio_manager.services.message_service import (
    send_message_api,
    get_message_logs_api,
    delete_message_api
)

def send_message(to_number: str, from_number: str, body: str):
    """
    Send a message via Twilio API.
    """
    return send_message_api(to_number, from_number, body)

def get_message_logs(limit: int = 50):
    """
    Retrieve message logs via Twilio API.
    """
    return get_message_logs_api(limit)

def delete_message(message_sid: str):
    """
    Delete a message via Twilio API.
    """
    return delete_message_api(message_sid)
