def handle_search_command():
    """Handle searching for available phone numbers."""
    from twilio_manager.cli.menus.phone.search_menu import SearchMenu
    SearchMenu().show()