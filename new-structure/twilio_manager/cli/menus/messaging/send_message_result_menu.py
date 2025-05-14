from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_success, print_error

class SendMessageResultMenu(BaseMenu):
    """Display the result of sending a message."""
    def __init__(self, parent, result):
        super().__init__(parent)
        self.result = result

    def show(self):
        self.clear_screen()
        self.show_header("📩 Message Result")
        if self.result.get("success"):
            print_success(f"Message sent! SID: {self.result.get('sid')}")
        else:
            print_error(f"Failed to send message: {self.result.get('error', 'Unknown error')}")
        self.wait_for_keypress()
        self.exit_to_parent()
