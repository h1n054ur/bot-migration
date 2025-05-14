from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.messaging.send_message_parameters_menu import SendMessageParametersMenu
from twilio_manager.cli.menus.messaging.send_message_result_menu import SendMessageResultMenu
from twilio_manager.core.messaging import send_message
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console

class SendMessageMenu(BaseMenu):
    """Handle sending a message."""
    def show(self):
        self.clear_screen()
        self.show_header("✉️ Send a Message")
        params = SendMessageParametersMenu(self).show()
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Sending message...", total=None)
            result = send_message(params["to"], params["from"], params["body"])
            progress.remove_task(task)
        SendMessageResultMenu(self, result).show()
