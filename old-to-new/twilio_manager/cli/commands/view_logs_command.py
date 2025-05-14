def handle_view_message_logs():
    """Display message logs."""
    from twilio_manager.cli.menus.messaging.message_logs_menu import MessageLogsMenu
    MessageLogsMenu().show()

def handle_view_call_logs():
    """Display call logs."""
    from twilio_manager.cli.menus.voice.call_logs_menu import CallLogsMenu
    CallLogsMenu().show()