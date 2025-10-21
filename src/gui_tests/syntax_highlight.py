from rich.console import Console
from rich.syntax import Syntax

console = Console()
with open("downloader.py", "rt") as code_file:
    syntax = Syntax(code_file.read(), "python")
console.print(syntax)
