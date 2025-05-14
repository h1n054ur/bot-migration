def handle_send_message_command():
    """Handle sending a message."""
    from twilio_manager.cli.menus.messaging.send_message_menu import SendMessageMenu
    SendMessageMenu().show()

def handle_delete_message_command():
    """Handle message deletion."""
    from twilio_manager.cli.menus.messaging.delete_message_menu import DeleteMessageMenu
    DeleteMessageMenu().show()