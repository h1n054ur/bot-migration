def handle_make_call_command():
    """Handle making a voice call."""
    from twilio_manager.cli.menus.voice.call_menu import CallMenu
    CallMenu().show()

def handle_manage_recordings():
    """Handle recording management."""
    from twilio_manager.cli.menus.voice.recordings_menu import RecordingsMenu
    RecordingsMenu().show()

def handle_conference_calls():
    """Handle conference call management."""
    from twilio_manager.cli.menus.voice.conference_menu import ConferenceMenu
    ConferenceMenu().show()