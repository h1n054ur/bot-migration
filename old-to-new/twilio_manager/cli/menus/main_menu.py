from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone_menu import PhoneMenu
from twilio_manager.cli.menus.messaging.messaging_menu import MessagingMenu
from twilio_manager.cli.menus.voice.voice_menu import VoiceMenu
from twilio_manager.cli.menus.account.account_menu import AccountMenu
from twilio_manager.cli.menus.advanced.advanced_menu import AdvancedMenu
from twilio_manager.shared.ui.styling import print_warning, print_info

class MainMenu(BaseMenu):
    """Main menu, entry point for the CLI."""
    def show(self):
        self.clear_screen()
        self.show_header("📂 Main Menu")
        print("1. Phone Number Management")
        print("2. Messaging")
        print("3. Voice")
        print("4. Account")
        print("5. Advanced")
        print("0. Exit")
        
        options = ["1", "2", "3", "4", "5", "0"]
        choice = self.prompt_choice(options, default="0")
        
        if choice == "1":
            PhoneMenu(self).show()
        elif choice == "2":
            MessagingMenu(self).show()
        elif choice == "3":
            VoiceMenu(self).show()
        elif choice == "4":
            AccountMenu(self).show()
        elif choice == "5":
            AdvancedMenu(self).show()
        elif choice == "0":
            print_info("Goodbye!")
        else:
            print_warning("Option not implemented yet.")
            self.show()
