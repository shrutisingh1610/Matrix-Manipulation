import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def start():
    os.system("python register.py")
def login():
    os.system("python login.py")

window = Tk()

window.title("Matrix Manipulation")
window.geometry("1000x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    500.0,
    407.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    407.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    60.0,
    49.0,
    image=image_image_3
)

canvas.create_text(
    17.0,
    617.0,
    anchor="nw",
    text="Mini Project",
    fill="#2B258C",
    font=("Inter Bold", 28 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start,
    relief="flat"
)
button_1.place(
    x=382.0,
    y=540.0,
    width=237.0,
    height=75.0
)

canvas.create_text(
    128.0,
    356.0,
    anchor="nw",
    text="Addition,Multiplication, Inverse and Transpose of Matrices",
    fill="#838383",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    163.0,
    407.0,
    anchor="nw",
    text="Project Contributed by: Rishabh Sinha, Pankaj Jaiswal, ",
    fill="#838383",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    243.0,
    443.0,
    anchor="nw",
    text="Ashutosh Shrivastava, Shruti Singh ",
    fill="#838383",
    font=("Inter Bold", 25 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_2.place(
    x=860.0,
    y=17.0,
    width=128.0,
    height=52.0
)
window.resizable(False, False)
window.mainloop()
