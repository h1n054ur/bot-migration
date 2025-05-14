from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.messaging.delete_message_parameters_menu import DeleteMessageParametersMenu
from twilio_manager.cli.menus.messaging.delete_message_result_menu import DeleteMessageResultMenu
from twilio_manager.core.messaging import delete_message
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console, prompt_choice, print_info

class DeleteMessageMenu(BaseMenu):
    """Handle deleting a message."""
    def show(self):
        self.clear_screen()
        self.show_header("🗑 Delete a Message")
        params = DeleteMessageParametersMenu(self).show()
        confirm = prompt_choice(
            ["y", "n"],
            default="n",
            prompt_text=f"Confirm delete of SID {params['sid']}? (y/n)"
        )
        if confirm.lower() != "y":
            print_info("Delete cancelled.")
            self.wait_for_keypress()
            return self.exit_to_parent()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Deleting message...", total=None)
            result = delete_message(params["sid"])
            progress.remove_task(task)

        DeleteMessageResultMenu(self, result).show()
