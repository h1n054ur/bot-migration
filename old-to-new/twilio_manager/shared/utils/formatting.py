def format_message_log_entry(log: dict) -> dict:
    """Format a single message log entry.
    
    Args:
        log (dict): Message log entry
        
    Returns:
        dict: Formatted log entry
    """
    return {
        'from': log.get("from", "—"),
        'to': log.get("to", "—"),
        'body': log.get("body", "")[:40] + "...",
        'status': log.get("status", "—"),
        'date_sent': log.get("date_sent", "—")
    }

def format_call_log_entry(log: dict) -> dict:
    """Format a single call log entry.
    
    Args:
        log (dict): Call log entry
        
    Returns:
        dict: Formatted log entry
    """
    return {
        'from': log.get("from", "—"),
        'to': log.get("to", "—"),
        'status': log.get("status", "—"),
        'duration': str(log.get("duration", "0")),
        'start_time': log.get("start_time", "—")
    }