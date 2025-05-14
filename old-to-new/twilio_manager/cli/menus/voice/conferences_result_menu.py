from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_table, print_info

class ConferencesResultMenu(BaseMenu):
    """Display list of conferences."""
    def __init__(self, parent, results):
        super().__init__(parent)
        self.results = results

    def show(self):
        self.clear_screen()
        self.show_header("🎟 Conferences List")
        if self.results:
            headers = list(self.results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in self.results]
            print_table(headers, rows)
        else:
            print_info("No conferences found.")
        self.wait_for_keypress()
        self.exit_to_parent()
