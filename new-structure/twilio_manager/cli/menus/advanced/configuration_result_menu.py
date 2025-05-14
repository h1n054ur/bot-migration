from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_success, print_error

class ConfigurationResultMenu(BaseMenu):
    """Display result of application configuration."""
    def __init__(self, parent, result):
        super().__init__(parent)
        self.result = result

    def show(self):
        self.clear_screen()
        self.show_header("⚙️ Configuration Result")
        if self.result.get("success"):
            print_success("Configuration updated:")
            for k, v in self.result.get("config", {}).items():
                print(f"{k} = {v}")
        else:
            print_error("Failed to update configuration.")
        self.wait_for_keypress()
        self.exit_to_parent()
