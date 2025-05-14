from twilio_manager.cli.menus.base_menu import BaseMenu

class MakeCallParametersMenu(BaseMenu):
    """Gather parameters for making a voice call."""
    def show(self):
        self.clear_screen()
        self.show_header("📞 Call Parameters")
        to_number = input("Enter destination number (E.164): ").strip()
        from_number = input("Enter your Twilio number (E.164): ").strip()
        url = input("Enter Voice URL (TwiML resource URL): ").strip()
        return {"to": to_number, "from": from_number, "url": url}
