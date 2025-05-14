from twilio_manager.services.voice_service import (
    make_call_api,
    get_conferences_api,
    get_recordings_api,
    get_call_logs_api,
    delete_recording_api,
    join_conference_api,
    end_conference_api
)

def make_call(from_number, to_number, voice_url) -> tuple[bool, str | None]:
    """Make a phone call.
    
    Args:
        from_number (str): Caller phone number
        to_number (str): Recipient phone number
        voice_url (str): URL for voice TwiML
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = make_call_api(from_number, to_number, voice_url)
        return success, None
    except Exception as e:
        return False, str(e)

def get_call_logs() -> tuple[list, str | None]:
    """Get call logs.
    
    Returns:
        tuple[list, str | None]: (call_logs, error_message)
    """
    try:
        logs = get_call_logs_api()
        return logs, None
    except Exception as e:
        return [], str(e)

def get_conferences(limit: int = 50) -> tuple[list, str | None]:
    """Get active conferences.
    
    Args:
        limit (int): Maximum number of conferences to return
        
    Returns:
        tuple[list, str | None]: (conferences_list, error_message)
    """
    try:
        conferences = get_conferences_api(limit)
        return conferences, None
    except Exception as e:
        return [], str(e)

def get_recordings(limit: int = 50) -> tuple[list, str | None]:
    """Get call recordings.
    
    Args:
        limit (int): Maximum number of recordings to return
        
    Returns:
        tuple[list, str | None]: (recordings_list, error_message)
    """
    try:
        recordings = get_recordings_api(limit)
        return recordings, None
    except Exception as e:
        return [], str(e)

def delete_recording(recording_sid: str) -> tuple[bool, str | None]:
    """Delete a recording by its SID.
    
    Args:
        recording_sid (str): Recording SID
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = delete_recording_api(recording_sid)
        return success, None
    except Exception as e:
        return False, str(e)

def join_conference(conference_sid: str, from_number: str) -> tuple[bool, str | None]:
    """Join a conference call.
    
    Args:
        conference_sid (str): Conference SID
        from_number (str): Phone number to join with
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = join_conference_api(conference_sid, from_number)
        return success, None
    except Exception as e:
        return False, str(e)

def end_conference(conference_sid: str) -> tuple[bool, str | None]:
    """End a conference call.
    
    Args:
        conference_sid (str): Conference SID
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        success = end_conference_api(conference_sid)
        return success, None
    except Exception as e:
        return False, str(e)
