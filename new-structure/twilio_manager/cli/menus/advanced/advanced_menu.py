from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.advanced.configuration_parameters_menu import ConfigurationParametersMenu
from twilio_manager.cli.menus.advanced.configuration_result_menu import ConfigurationResultMenu
from twilio_manager.cli.menus.advanced.advanced_search_menu import AdvancedSearchMenu
from twilio_manager.shared.ui.styling import print_warning
from twilio_manager.core.advanced import configure_app

class AdvancedMenu(BaseMenu):
    """Advanced menu: routes to advanced sub-flows."""
    def show(self):
        self.clear_screen()
        self.show_header("🚀 Advanced")
        print("1. Configuration")
        print("2. Search Resources")
        print("0. 🔙 Back")
        options = ["1", "2", "0"]
        choice = self.prompt_choice(options, default="0")
        if choice == "1":
            config = ConfigurationParametersMenu(self).show()
            result = configure_app(config)
            ConfigurationResultMenu(self, result).show()
        elif choice == "2":
            AdvancedSearchMenu(self).show()
        elif choice == "0":
            self.exit_to_parent()
        else:
            print_warning("Option not implemented yet.")
            self.show()
