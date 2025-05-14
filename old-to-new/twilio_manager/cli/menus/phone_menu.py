from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone.search_menu import SearchMenu
from twilio_manager.shared.ui.styling import print_warning

class PhoneMenu(BaseMenu):
    """Phone menu: routes to phone number sub-flows."""
    def show(self):
        self.clear_screen()
        self.show_header("📞 Phone Number Management")
        print("1. 🔍 Search Available Numbers")
        print("2. 🛒 Purchase a Number")
        print("3. ⚙️ Configure a Number")
        print("4. 🗑 Release a Number")
        print("0. 🔙 Back")
        options = ["1", "2", "3", "4", "0"]
        choice = self.prompt_choice(options, default="0")
        if choice == "1":
            SearchMenu(self).show()
        elif choice == "0":
            self.exit_to_parent()
        else:
            print_warning("Option not implemented yet.")
            self.show()
