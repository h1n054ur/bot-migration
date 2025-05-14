from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone.release_parameters_menu import ReleaseParametersMenu
from twilio_manager.cli.menus.phone.release_result_menu import ReleaseResultMenu
from twilio_manager.core.phone_numbers import release_number
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console, prompt_choice, print_info

class ReleaseMenu(BaseMenu):
    """Handle releasing a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("🗑 Release a Number")
        params = ReleaseParametersMenu(self).show()

        # Confirmation prompt
        confirm = prompt_choice(
            ["y", "n"],
            default="n",
            prompt_text=f"Confirm release of {params['phone_number']}? (y/n)"
        )
        if confirm.lower() != "y":
            print_info("Release cancelled.")
            self.wait_for_keypress()
            return self.exit_to_parent()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Releasing phone number...", total=None)
            result = release_number(params["phone_number"])
            progress.remove_task(task)

        ReleaseResultMenu(self, result).show()
