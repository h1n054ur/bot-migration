from twilio_manager.cli.menus.base_menu import BaseMenu

class PurchaseParametersMenu(BaseMenu):
    """Gather parameters for purchasing a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("🛒 Purchase Parameters")
        phone_number = input("Enter the phone number to purchase (E.164 format): ").strip()
        return {"phone_number": phone_number}
