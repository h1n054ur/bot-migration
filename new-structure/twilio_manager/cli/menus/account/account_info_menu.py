from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.core.account import get_account_info
from twilio_manager.shared.ui.styling import console, print_table, print_info
from rich.progress import Progress, SpinnerColumn, TextColumn

class AccountInfoMenu(BaseMenu):
    """Display account information."""
    def show(self):
        self.clear_screen()
        self.show_header("ℹ️ Account Info")
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console, transient=True) as progress:
            task = progress.add_task("Fetching account info...", total=None)
            result = get_account_info()
            progress.remove_task(task)

        if result:
            headers = list(result.keys())
            rows = [[str(result.get(h, "")) for h in headers]]
            print_table(headers, rows)
        else:
            print_info("No account info available.")
        self.wait_for_keypress()
        self.exit_to_parent()
