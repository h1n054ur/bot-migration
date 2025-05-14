from twilio.rest import Client
from twilio_manager.shared.config import ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def make_call_api(from_number, to_number, voice_url) -> tuple[bool, str | None]:
    """Make a phone call using Twilio API.
    
    Args:
        from_number (str): Caller phone number
        to_number (str): Recipient phone number
        voice_url (str): URL for voice TwiML
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url=voice_url
        )
        return bool(call and call.sid), None
    except Exception as e:
        return False, str(e)

def get_call_logs_api(limit=20) -> tuple[list, str | None]:
    """Fetch call logs from Twilio API.
    
    Args:
        limit (int): Maximum number of logs to fetch
        
    Returns:
        tuple[list, str | None]: (call_logs, error_message)
    """
    try:
        calls = client.calls.list(limit=limit)
        logs = [
            {
                "from": c.from_,
                "to": c.to,
                "status": c.status,
                "duration": c.duration,
                "start_time": str(c.start_time)
            } for c in calls
        ]
        return logs, None
    except Exception as e:
        return [], str(e)

def get_conferences_api(limit: int = 50) -> tuple[list, str | None]:
    """Get active conferences from Twilio API.
    
    Args:
        limit (int): Maximum number of conferences to return
        
    Returns:
        tuple[list, str | None]: (conferences_list, error_message)
    """
    try:
        conferences = client.conferences.list(limit=limit)
        conf_list = [
            {
                "sid": c.sid,
                "friendly_name": c.friendly_name,
                "status": c.status,
                "participants": len(list(c.participants.list())),
                "start_time": str(c.date_created)
            } for c in conferences
        ]
        return conf_list, None
    except Exception as e:
        return [], str(e)

def get_recordings_api(limit: int = 50) -> tuple[list, str | None]:
    """Get call recordings from Twilio API.
    
    Args:
        limit (int): Maximum number of recordings to return
        
    Returns:
        tuple[list, str | None]: (recordings_list, error_message)
    """
    try:
        recordings = client.recordings.list(limit=limit)
        rec_list = [
            {
                "sid": r.sid,
                "duration": r.duration,
                "channels": r.channels,
                "status": r.status,
                "date_created": str(r.date_created),
                "url": r.media_url
            } for r in recordings
        ]
        return rec_list, None
    except Exception as e:
        return [], str(e)

def delete_recording_api(recording_sid: str) -> tuple[bool, str | None]:
    """Delete a recording using Twilio API.
    
    Args:
        recording_sid (str): Recording SID to delete
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        recording = client.recordings(recording_sid).delete()
        return True, None
    except Exception as e:
        return False, str(e)

def join_conference_api(conference_sid: str, from_number: str) -> tuple[bool, str | None]:
    """Join a conference call using Twilio API.
    
    Args:
        conference_sid (str): Conference SID to join
        from_number (str): Phone number to join with
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        # Create a call that joins the conference
        call = client.calls.create(
            to=from_number,
            from_=from_number,  # Use same number as caller ID
            twiml=f'<Response><Dial><Conference>{conference_sid}</Conference></Dial></Response>'
        )
        return bool(call and call.sid), None
    except Exception as e:
        return False, str(e)

def end_conference_api(conference_sid: str) -> tuple[bool, str | None]:
    """End a conference call using Twilio API.
    
    Args:
        conference_sid (str): Conference SID to end
        
    Returns:
        tuple[bool, str | None]: (success, error_message)
    """
    try:
        # Update conference status to completed
        conference = client.conferences(conference_sid).update(status='completed')
        return bool(conference and conference.sid), None
    except Exception as e:
        return False, str(e)
