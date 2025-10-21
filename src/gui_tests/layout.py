from rich import print
from rich.layout import Layout

layout = Layout()
print(layout)

layout.split_column(Layout(name="upper"), Layout(name="lower"))
print(layout)


layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
)
print(layout)


layout["left"].update(
    "The mystery of life isn't a problem to solve, but a reality to experience."
)
print(layout)
layout["upper"].size = 10
print(layout)


layout["upper"].size = 10
print(layout)
