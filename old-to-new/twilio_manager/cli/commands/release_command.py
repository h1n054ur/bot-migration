def handle_release_command():
    """Handle the release of a phone number."""
    from twilio_manager.cli.menus.phone.release_menu import ReleaseMenu
    ReleaseMenu().show()