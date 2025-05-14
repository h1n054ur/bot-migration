from twilio_manager.cli.menus.base_menu import BaseMenu

class ReleaseParametersMenu(BaseMenu):
    """Gather parameters for releasing a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("🗑 Release Parameters")
        phone_number = input("Enter the phone number to release (E.164 format): ").strip()
        return {"phone_number": phone_number}
