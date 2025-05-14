from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.shared.ui.styling import print_error, print_table

class SearchResultsMenu(BaseMenu):
    """Display search results for available phone numbers."""
    def __init__(self, parent, results):
        super().__init__(parent)
        self.results = results

    def show(self):
        self.clear_screen()
        self.show_header("📋 Search Results")
        if not self.results:
            print_error("No numbers found matching your criteria.")
        else:
            # Dynamically extract headers and row data
            headers = list(self.results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in self.results]
            print_table(headers, rows)
        self.wait_for_keypress()
        self.exit_to_parent()
