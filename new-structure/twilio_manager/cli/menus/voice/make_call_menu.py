from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.voice.make_call_parameters_menu import MakeCallParametersMenu
from twilio_manager.cli.menus.voice.make_call_result_menu import MakeCallResultMenu
from twilio_manager.core.voice import make_call
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console

class MakeCallMenu(BaseMenu):
    """Handle making a voice call."""
    def show(self):
        self.clear_screen()
        self.show_header("📞 Make a Call")
        params = MakeCallParametersMenu(self).show()
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Placing call...", total=None)
            result = make_call(params["to"], params["from"], params["url"])
            progress.remove_task(task)
        MakeCallResultMenu(self, result).show()
