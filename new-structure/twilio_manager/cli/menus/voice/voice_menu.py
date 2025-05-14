from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.voice.make_call_menu import MakeCallMenu
from twilio_manager.cli.menus.voice.conferences_menu import ConferencesMenu
from twilio_manager.cli.menus.voice.recordings_menu import RecordingsMenu
from twilio_manager.cli.menus.voice.call_logs_menu import CallLogsMenu
from twilio_manager.shared.ui.styling import print_warning

class VoiceMenu(BaseMenu):
    """Voice menu: routes to voice sub-flows."""
    def show(self):
        self.clear_screen()
        self.show_header("📞 Voice")
        print("1. Make a Call")
        print("2. Conferences")
        print("3. Recordings")
        print("4. Call Logs")
        print("0. 🔙 Back")
        options = ["1", "2", "3", "4", "0"]
        choice = self.prompt_choice(options, default="0")
        if choice == "1":
            MakeCallMenu(self).show()
        elif choice == "2":
            ConferencesMenu(self).show()
        elif choice == "3":
            RecordingsMenu(self).show()
        elif choice == "4":
            CallLogsMenu(self).show()
        elif choice == "0":
            self.exit_to_parent()
        else:
            print_warning("Option not implemented yet.")
            self.show()
