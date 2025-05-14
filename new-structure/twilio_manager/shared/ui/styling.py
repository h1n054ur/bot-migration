from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

console = Console()

def print_panel(title: str, content: str = ""):
    """
    Render a header panel with optional content below.
    """
    panel = Panel(Text(content), title=title, expand=True)
    console.clear()
    console.print(panel)

def print_success(message: str):
    console.print(f"[bold green]✔ {message}[/]")

def print_error(message: str):
    console.print(f"[bold red]✖ {message}[/]")

def print_warning(message: str):
    console.print(f"[bold yellow]⚠ {message}[/]")

def print_info(message: str):
    console.print(f"[bold cyan]ℹ {message}[/]")

def prompt_choice(options: list[str], default: str = None, prompt_text: str = "Choose an option") -> str:
    """
    Prompt the user to select one choice from a list.
    """
    choice = Prompt.ask(
        prompt_text,
        choices=options,
        default=default,
        show_choices=True
    )
    return choice

def print_table(headers: list[str], rows: list[list[str]]):
    """
    Render a simple table given headers and row data.
    
    - headers: list of column titles
    - rows: list of rows, where each row is a list of strings
    """
    table = Table(show_header=True, header_style="bold magenta")
    for h in headers:
        table.add_column(h)
    for row in rows:
        table.add_row(*row)
    console.print(table)
