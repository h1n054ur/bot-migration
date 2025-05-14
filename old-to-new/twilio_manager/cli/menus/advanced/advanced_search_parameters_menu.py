from twilio_manager.cli.menus.base_menu import BaseMenu

class AdvancedSearchParametersMenu(BaseMenu):
    """Gather query for advanced search."""
    def show(self):
        self.clear_screen()
        self.show_header("🔍 Enter Search Query")
        query = input("Search query: ").strip()
        return query
