from twilio_manager.shared.ui.styling import console, print_panel, print_success, print_error, print_warning, print_info, prompt_choice

class BaseMenu:
    """Base class for all menus, handling display and user input."""
    def __init__(self, parent=None):
        self.parent = parent

    def clear_screen(self):
        """Clear the terminal screen."""
        console.clear()

    def show_header(self, title: str):
        """Display the menu header."""
        print_panel(title)

    def show(self):
        """Main loop for the menu. Should be overridden by subclasses."""
        raise NotImplementedError

    def prompt_choice(self, options: list[str], default: str = None, prompt_text: str = "Choose an option") -> str:
        """
        Prompt the user to select one choice from a list.
        """
        return prompt_choice(options, default, prompt_text)

    def wait_for_keypress(self):
        """Wait for user to press Enter."""
        input("\nPress Enter to continue...")

    def exit_to_parent(self):
        """Return to parent menu."""
        if self.parent:
            self.parent.show()
