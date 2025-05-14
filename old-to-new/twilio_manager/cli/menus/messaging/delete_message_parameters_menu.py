from twilio_manager.cli.menus.base_menu import BaseMenu

class DeleteMessageParametersMenu(BaseMenu):
    """Gather parameters for deleting a message."""
    def show(self):
        self.clear_screen()
        self.show_header("🗑 Delete Parameters")
        sid = input("Enter Message SID to delete: ").strip()
        return {"sid": sid}
