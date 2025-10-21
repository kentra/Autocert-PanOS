# import time
# from rich.progress import track
# from rich.progress import Progress

# with Progress() as progress:

#     task1 = progress.add_task("[red]Downloading...", total=1000)
#     task2 = progress.add_task("[green]Processing...", total=1000)
#     task3 = progress.add_task("[cyan]Cooking...", total=1000)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)


# for i in track(range(20), description="Processing..."):
#     time.sleep(1)  # Simulate work being done


# progress = Progress()
# progress.start()
# try:
#     task1 = progress.add_task("[red]Downloading...", total=1000)
#     task2 = progress.add_task("[green]Processing...", total=1000)
#     task3 = progress.add_task("[cyan]Cooking...", total=1000)

#     while not progress.finished:
#         progress.update(task1, advance=0.5)
#         progress.update(task2, advance=0.3)
#         progress.update(task3, advance=0.9)
#         time.sleep(0.02)
# finally:
#     progress.stop()


# with Progress(transient=True, refresh_per_second=20, auto_refresh=True) as progress:
#     task = progress.add_task("Working", total=100, start=True)
#     time.sleep(10)


# from time import sleep

# from rich.table import Column
# from rich.progress import Progress, BarColumn, TextColumn

# text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
# bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
# progress = Progress(text_column, bar_column, expand=True)

# with progress:
#     for n in progress.track(range(100)):
#         progress.print(n)
#         sleep(0.1)


# from time import sleep

# from rich.table import Column
# from rich.progress import Progress, BarColumn, TextColumn

# text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
# bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
# progress = Progress(text_column, bar_column, expand=True)

# with Progress() as progress:
#     task = progress.add_task("twiddling thumbs", total=10)
#     for job in range(10):
#         progress.console.print(f"Working on job #{job}")
#         # run_job(job)
#         sleep(0.4)
#         progress.advance(task)


# from rich.panel import Panel
# from rich.progress import Progress


# class MyProgress(Progress):
#     def get_renderables(self):
#         yield Panel(self.make_tasks_table(self.tasks))
