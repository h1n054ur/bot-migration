from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.core.account import list_sip_trunks
from twilio_manager.shared.ui.styling import console, print_table, print_info
from rich.progress import Progress, SpinnerColumn, TextColumn

class SipTrunksMenu(BaseMenu):
    """Display SIP Trunks."""
    def show(self):
        self.clear_screen()
        self.show_header("📶 SIP Trunks")
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console, transient=True) as progress:
            task = progress.add_task("Fetching SIP trunks...", total=None)
            results = list_sip_trunks()
            progress.remove_task(task)

        if results:
            headers = list(results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in results]
            print_table(headers, rows)
        else:
            print_info("No SIP trunks found.")
        self.wait_for_keypress()
        self.exit_to_parent()
