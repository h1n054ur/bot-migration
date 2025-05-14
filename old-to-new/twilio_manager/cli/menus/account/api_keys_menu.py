from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.core.account import list_api_keys
from twilio_manager.shared.ui.styling import console, print_table, print_info
from rich.progress import Progress, SpinnerColumn, TextColumn

class ApiKeysMenu(BaseMenu):
    """Display API keys."""
    def show(self):
        self.clear_screen()
        self.show_header("🔑 API Keys")
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console, transient=True) as progress:
            task = progress.add_task("Fetching API keys...", total=None)
            results = list_api_keys()
            progress.remove_task(task)

        if results:
            headers = list(results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in results]
            print_table(headers, rows)
        else:
            print_info("No API keys found.")
        self.wait_for_keypress()
        self.exit_to_parent()
