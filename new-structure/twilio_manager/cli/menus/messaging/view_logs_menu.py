from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.core.messaging import get_message_logs
from twilio_manager.shared.ui.styling import console, print_table, print_info
from rich.progress import Progress, SpinnerColumn, TextColumn

class ViewLogsMenu(BaseMenu):
    """Handle viewing message logs."""
    def show(self):
        self.clear_screen()
        self.show_header("📜 Message Logs")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Fetching message logs...", total=None)
            results = get_message_logs()
            progress.remove_task(task)

        if results:
            headers = list(results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in results]
            print_table(headers, rows)
        else:
            print_info("No message logs found.")
        self.wait_for_keypress()
        self.exit_to_parent()
