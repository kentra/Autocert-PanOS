from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    DownloadColumn,
    FileSizeColumn,
    MofNCompleteColumn,
)
from rich.progress_bar import ProgressBar
from rich.syntax import Syntax
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["side"].split(Layout(name="box1"), Layout(name="box2"))
    return layout


class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]Autocert[/b] Let's Encrypt Palo Alto",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style=" black")


def main_screen() -> Panel:
    """Some example content."""
    code = """\
# Caching

## Dependency caching

uv uses aggressive caching to avoid re-downloading (and re-building) dependencies that have already been accessed in prior runs.

The specifics of uv's caching semantics vary based on the nature of the dependency:

For registry dependencies (like those downloaded from PyPI), uv respects HTTP caching headers.
For direct URL dependencies, uv respects HTTP caching headers, and also caches based on the URL itself.
For Git dependencies, uv caches based on the fully-resolved Git commit hash. As such, uv pip compile will pin Git dependencies to a specific commit hash when writing the resolved dependency set.
For local dependencies, uv caches based on the last-modified time of the source archive (i.e., the local .whl or .tar.gz file). For directories, uv caches based on the last-modified time of the pyproject.toml, setup.py, or setup.cfg file.
If you're running into caching issues, uv includes a few escape hatches:

To clear the cache entirely, run uv cache clean. To clear the cache for a specific package, run uv cache clean <package-name>. For example, uv cache clean ruff will clear the cache for the ruff package.
To force uv to revalidate cached data for all dependencies, pass --refresh to any command (e.g., uv sync --refresh or uv pip install --refresh ...).
To force uv to revalidate cached data for a specific dependency pass --refresh-package to any command (e.g., uv sync --refresh-package ruff or uv pip install --refresh-package ruff ...).
To force uv to ignore existing installed versions, pass --reinstall to any installation command (e.g., uv sync --reinstall or uv pip install --reinstall ...). (Consider running uv cache clean <package-name> first, to ensure that the cache is cleared prior to reinstallation.)
As a special case, uv will always rebuild and reinstall any local directory dependencies passed explicitly on the command-line (e.g., uv pip install .).


    """
    syntax = Syntax(code, "markdown", line_numbers=True, dedent=True)
    main_screen_item = Table.grid(padding=0, expand=True)
    # main_screen_item.add_column(style="green", justify="right")
    # main_screen_item.add_column(no_wrap=True)
    message = Table.grid(padding=0)
    # message.add_column()
    # message.add_column(no_wrap=True)
    message.add_row(main_screen_item)

    message_panel = Panel(
        Align.center(
            # Group(Align.center(main_screen_item)),
            Group(Align.center(syntax)),
            vertical="top",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b green]Logs!",
        # border_style="bright_blue",
        border_style="black",
    )
    return message_panel


def main_menu():
    main_menu_item = Table.grid(padding=0)
    main_menu_item.add_column(style="green", justify="right")
    main_menu_item.add_column(no_wrap=True)
    main_menu_item.add_row(f"[bold green]1[/bold green]]", f"[yellow]Certbot[/yellow]")
    main_menu_item.add_row(
        f"[bold green]2[/bold green]]", f"[yellow]Renew Certificate[/yellow]"
    )
    main_menu_item.add_row(
        f"[bold green]3[/bold green]]", f"[yellow]Check Expiration Date[/yellow]"
    )
    main_menu_item.add_row(f"[bold green]4[/bold green]]", f"[yellow]Exit[/yellow]")

    menu_container = Table.grid(padding=0)
    menu_container.add_column()
    menu_container.add_column(no_wrap=True)
    menu_container.add_row(main_menu_item)

    menu_panel = Panel(
        Align.center(
            Group(Align.center(main_menu_item)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Main menu!",
        # border_style="bright_blue",
        border_style="black",
    )
    return menu_panel


job_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
job_progress.add_task("[green]CPU")
job_progress.add_task("[magenta]RAM", total=200)
job_progress.add_task("[cyan]MEM", total=400)

total = sum(task.total for task in job_progress.tasks)
overall_progress = Progress(
    f"[progress] {job_progress.speed_estimate_period}",
    SpinnerColumn(),
    BarColumn(),
)
overall_task = overall_progress.add_task("All Jobs", total=int(total))

progress_table = Table.grid(expand=True)
progress_table.add_row(
    Panel(
        overall_progress,
        title="Overall Progress",
        border_style="green",
        padding=(2, 2),
    ),
    Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
)


# Make magic
layout = make_layout()
layout["header"].update(Header())
layout["body"].update(Panel(main_screen(), border_style="magenta"))
# layout["box2"].update(Panel(testProgress, border_style="green"))
layout["box1"].update(Panel(main_menu(), border_style="red"))
layout["footer"].update(progress_table)


from time import sleep
from random import randint

from rich.live import Live

with Live(layout, refresh_per_second=10, screen=True):

    while True:
        sleep(0.1)

        for job in job_progress.tasks:
            if not job.finished:
                job_progress.advance(job.id)

        completed = sum(task.completed for task in job_progress.tasks)
        overall_progress.update(
            overall_task,
            completed=completed,
        )
        # overall_progress.update(rand)
