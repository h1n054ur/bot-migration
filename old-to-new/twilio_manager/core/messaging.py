from twilio_manager.services.message_service import (
    send_message_api,
    get_message_logs_api,
    delete_message_api,
    get_recent_contacts_api
)

def validate_recipient_number(number: str) -> bool:
    """Validate the recipient's phone number format.
    
    Args:
        number (str): Phone number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    # Basic E.164 format validation
    if not number.startswith('+'):
        return False
    if not number[1:].isdigit():
        return False
    if len(number) < 8 or len(number) > 15:  # E.164 length limits
        return False
    return True

def send_message(from_number, to_number, body) -> tuple[bool, str | None]:
    """Send a message.
    
    Args:
        from_number (str): Sender phone number
        to_number (str): Recipient phone number
        body (str): Message content
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = send_message_api(from_number, to_number, body)
        return success, None
    except Exception as e:
        return False, str(e)

def get_message_logs() -> tuple[list, str | None]:
    """Get message logs.
    
    Returns:
        tuple[list, str | None]: (message_logs, error_message)
    """
    try:
        logs = get_message_logs_api()
        return logs, None
    except Exception as e:
        return [], str(e)

def get_recent_contacts(limit=10) -> tuple[list, str | None]:
    """Get a list of unique recent contacts.
    
    Args:
        limit (int): Maximum number of contacts to return
        
    Returns:
        tuple[list, str | None]: (contacts_list, error_message)
    """
    try:
        contacts = get_recent_contacts_api(limit)
        return contacts, None
    except Exception as e:
        return [], str(e)

def delete_message(message_sid: str) -> tuple[bool, str | None]:
    """Delete a message.
    
    Args:
        message_sid (str): The SID of the message to delete
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = delete_message_api(message_sid)
        return success, None
    except Exception as e:
        return False, str(e)
