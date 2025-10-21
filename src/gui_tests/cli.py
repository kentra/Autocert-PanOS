# from crud.certbot_wrapper import CertbotWrapper
# from crud.panos_tools import PanosTools
# from crud.cert_tools import CertTools
# from models.config import CertBot, Panos
# from log_handler import logger
# from models.palo_xml_api import Certficate


import rich_click as click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.theme import Theme
from rich.pretty import pprint
import logging
from rich.logging import RichHandler
from rich.traceback import install
from rich.prompt import Prompt
from rich import print
from rich.console import Group
from rich.panel import Panel

panel_group = Group(
    Panel("Hello", style="on blue"),
    Panel("World", style="on red"),
)
print(Panel(panel_group))
install(show_locals=True)


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")
# Use Rich markup
click.rich_click.USE_RICH_MARKUP = True


console = Console()


@click.command()
@click.rich_config({"theme": "nord-slim", "enable_theme_env_var": False})
def menu():
    console.print()
    console.print(
        Panel("Whaat", title_align="center"),
        Panel(
            "\n[bold underline2 magenta]Autocert[/bold underline2 magenta] - By Daniel Kolstad\n[yellow]A Certbot product[/yellow]\n\n[bold cyan]Main Menu[/bold cyan]\nChoose an option:"
        ),
    )

    pprint(locals())
    console.print("Google", style="link https://google.com")
    console.print("Hello", style="magenta bold")
    help_config = {"text_markup": "rich bold"}

    options = {"1": "Run Certbot", "2": "Get expiratin date Palo", "4": "Exit"}

    console.print(
        "\n".join(
            [
                f"[bold green]{key}[/bold green]] {value}"
                for key, value in options.items()
            ]
        )
    )

    choice = Prompt.ask("\nEnter your choice", choices=list(options.keys()))

    if choice == "1":
        console.print(Panel("[bold yellow]System Status: All good ✅"))
    elif choice == "2":
        console.print(Panel("[bold magenta]Process Started..."))
    else:
        console.print("[bold red]Goodbye!")


if __name__ == "__main__":
    menu()
