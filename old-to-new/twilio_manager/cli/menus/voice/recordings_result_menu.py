from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_table, print_error

class RecordingsResultMenu(BaseMenu):
    """Display recordings for a conference."""
    def __init__(self, parent, results):
        super().__init__(parent)
        self.results = results

    def show(self):
        self.clear_screen()
        self.show_header("🎙 Recordings List")
        if not self.results:
            print_error("No recordings found.")
        else:
            headers = list(self.results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in self.results]
            print_table(headers, rows)
        self.wait_for_keypress()
        self.exit_to_parent()
