from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_warning

class ConfigureParametersMenu(BaseMenu):
    """Gather parameters for configuring a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("⚙️ Configure Parameters")
        phone_number = input("Enter the phone number to configure (E.164 format): ").strip()

        # Placeholder for configuration options (e.g., webhook URLs, SMS handler)
        print("\nEnter configuration settings as key=value, one per line. Leave blank to finish.")
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

        return {"phone_number": phone_number, "config": config}
