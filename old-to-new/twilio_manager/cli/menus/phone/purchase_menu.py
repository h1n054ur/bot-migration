from twilio_manager.cli.menus.base_menu import BaseMenu
from twilio_manager.cli.menus.phone.purchase_parameters_menu import PurchaseParametersMenu
from twilio_manager.cli.menus.phone.purchase_result_menu import PurchaseResultMenu
from twilio_manager.core.phone_numbers import purchase_number
from rich.progress import Progress, SpinnerColumn, TextColumn
from twilio_manager.shared.ui.styling import console, prompt_choice, print_info, print_warning

class PurchaseMenu(BaseMenu):
    """Handle purchasing a phone number."""
    def show(self):
        self.clear_screen()
        self.show_header("🛒 Purchase a Number")
        params = PurchaseParametersMenu(self).show()

        # Confirmation prompt
        confirm = prompt_choice(
            ["y", "n"],
            default="n",
            prompt_text=f"Confirm purchase of {params['phone_number']}? (y/n)"
        )
        if confirm.lower() != "y":
            print_info("Purchase cancelled.")
            self.wait_for_keypress()
            return self.exit_to_parent()

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Purchasing phone number...", total=None)
            result = purchase_number(params["phone_number"])
            progress.remove_task(task)

        PurchaseResultMenu(self, result).show()
