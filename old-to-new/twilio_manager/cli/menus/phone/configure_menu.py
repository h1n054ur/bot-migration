from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone.configure_parameters_menu import ConfigureParametersMenu
from twilio_manager.cli.menus.phone.configure_result_menu import ConfigureResultMenu
from twilio_manager.core.phone_numbers import configure_number
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console

class ConfigureMenu(BaseMenu):
    """Handle configuring a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("⚙️ Configure a Number")
        params = ConfigureParametersMenu(self).show()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Configuring phone number...", total=None)
            result = configure_number(params["phone_number"], params["config"])
            progress.remove_task(task)

        ConfigureResultMenu(self, result).show()
