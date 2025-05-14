from twilio_manager.cli.menus.base_menu import BaseMenu

class SendMessageParametersMenu(BaseMenu):
    """Gather parameters for sending a message."""
    def show(self):
        self.clear_screen()
        self.show_header("✉️ Message Parameters")
        to_number = input("Enter destination number (E.164): ").strip()
        from_number = input("Enter your Twilio number (E.164): ").strip()
        body = input("Enter message body: ").strip()
        return {"to": to_number, "from": from_number, "body": body}
