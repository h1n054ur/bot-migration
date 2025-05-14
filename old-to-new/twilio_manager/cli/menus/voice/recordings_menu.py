from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.core.voice import get_recordings
from twilio_manager.shared.ui.styling import console, print_table, print_info
from rich.progress import Progress, SpinnerColumn, TextColumn

class RecordingsMenu(BaseMenu):
    """Handle listing recordings."""
    def show(self):
        self.clear_screen()
        self.show_header("🎞️ Recordings")
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Fetching recordings...", total=None)
            results = get_recordings()
            progress.remove_task(task)

        if results:
            headers = list(results[0].keys())
            rows = [[str(item.get(h, "")) for h in headers] for item in results]
            print_table(headers, rows)
        else:
            print_info("No recordings found.")
        self.wait_for_keypress()
        self.exit_to_parent()
