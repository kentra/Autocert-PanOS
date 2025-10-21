MARKDOWN = """
# This is an h1

Rich can do a pretty *decent* job of rendering markdown.

1. This is a list item
2. This is another list item
"""
from rich.console import Console
from rich.markdown import Markdown
from rich import print
from rich.padding import Padding
from rich import print
from rich.panel import Panel
import time
from rich.progress import track

test = Padding("Hello PADDING", (2, 4))
print(test)
from rich import print
from rich.padding import Padding

test = Padding("MEIR PÆDDING", (2, 4), style="on blue", expand=False)
print(test)
for i in track(range(20), description="Processing..."):
    time.sleep(1)  # Simulate work being done

print(Panel("Hello, [red]World!"))
console = Console()
md = Markdown(MARKDOWN)
console.print(md)
