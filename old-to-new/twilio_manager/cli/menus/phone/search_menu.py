from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone.search_parameters_menu import SearchParametersMenu
from twilio_manager.cli.menus.phone.search_results_menu import SearchResultsMenu
from twilio_manager.core.phone_numbers import search_available_numbers
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console

class SearchMenu(BaseMenu):
    """Orchestrate the search for available phone numbers."""
    def show(self):
        self.clear_screen()
        self.show_header("🔍 Search Available Numbers")
        params = SearchParametersMenu(self).show()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Searching for available numbers...", total=None)
            results = search_available_numbers(
                params["country_code"],
                number_type=params["number_type"],
                capabilities=params["capabilities"],
                pattern=params["pattern"],
            )
            progress.remove_task(task)

        SearchResultsMenu(self, results).show()
