from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_warning

class ConfigurationParametersMenu(BaseMenu):
    """Gather application configuration parameters."""
    def show(self):
        self.clear_screen()
        self.show_header("⚙️ Configuration")
        print("Enter configuration settings as key=value, one per line. Leave blank to finish.")
        config = {}
        while True:
            line = input().strip()
            if not line:
                break
            if "=" not in line:
                print_warning("Invalid format. Use key=value.")
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
        return config
