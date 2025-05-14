from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.advanced.advanced_search_parameters_menu import AdvancedSearchParametersMenu
from twilio_manager.cli.menus.advanced.advanced_search_results_menu import AdvancedSearchResultsMenu
from twilio_manager.core.advanced import search_resources
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console

class AdvancedSearchMenu(BaseMenu):
    """Handle advanced resource search."""
    def show(self):
        self.clear_screen()
        self.show_header("🔍 Advanced Search")
        query = AdvancedSearchParametersMenu(self).show()
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console, transient=True) as progress:
            task = progress.add_task("Searching resources...", total=None)
            results = search_resources(query)
            progress.remove_task(task)
        AdvancedSearchResultsMenu(self, results).show()
