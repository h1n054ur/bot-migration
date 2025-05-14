from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_success, print_error

class MakeCallResultMenu(BaseMenu):
    """Display the result of making a call."""
    def __init__(self, parent, result):
        super().__init__(parent)
        self.result = result

    def show(self):
        self.clear_screen()
        self.show_header("📞 Call Result")
        if self.result.get("success"):
            print_success(f"Call placed! SID: {self.result.get('sid')}")
        else:
            print_error(f"Failed to place call: {self.result.get('error', 'Unknown error')}")
        self.wait_for_keypress()
        self.exit_to_parent()
