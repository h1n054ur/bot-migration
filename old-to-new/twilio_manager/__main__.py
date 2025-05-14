from twilio_manager.cli.menus.main_menu import MainMenu
from twilio_manager.shared.ui.styling import console, clear_screen
import sys

def run_cli():
    """Entry point for the CLI application."""
    try:
        clear_screen()
        main_menu = MainMenu()
        main_menu.show()
    except KeyboardInterrupt:
        console.print("\n[red]Exited by user.[/red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    run_cli()
