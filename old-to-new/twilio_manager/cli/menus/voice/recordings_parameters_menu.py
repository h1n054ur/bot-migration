from twilio_manager.cli.menus.base_menu import BaseMenu

class RecordingsParametersMenu(BaseMenu):
    """Gather parameters for listing recordings."""
    def show(self):
        self.clear_screen()
        self.show_header("🎙 Recordings Parameters")
        sid = input("Enter Conference SID: ").strip()
        return {"conference_sid": sid}
