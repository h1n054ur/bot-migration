from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.messaging.send_message_menu import SendMessageMenu
from twilio_manager.cli.menus.messaging.view_logs_menu import ViewLogsMenu
from twilio_manager.cli.menus.messaging.delete_message_menu import DeleteMessageMenu
from twilio_manager.shared.ui.styling import print_warning

class MessagingMenu(BaseMenu):
    """Messaging menu: routes to messaging sub-flows."""
    def show(self):
        self.clear_screen()
        self.show_header("✉️ Messaging")
        print("1. Send a Message")
        print("2. View Message Logs")
        print("3. Delete a Message")
        print("0. 🔙 Back")
        options = ["1", "2", "3", "0"]
        choice = self.prompt_choice(options, default="0")
        if choice == "1":
            SendMessageMenu(self).show()
        elif choice == "2":
            ViewLogsMenu(self).show()
        elif choice == "3":
            DeleteMessageMenu(self).show()
        elif choice == "0":
            self.exit_to_parent()
        else:
            print_warning("Option not implemented yet.")
            self.show()
