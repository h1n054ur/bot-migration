def handle_configure_command():
    """Handle the configuration of a phone number."""
    from twilio_manager.cli.menus.phone.configure_menu import ConfigureMenu
    ConfigureMenu().show()