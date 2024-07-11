import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def login():
    os.system("python dashboard.py")

window = Tk()

window.title("Login")
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
canvas.create_text(
    622.0,
    43.0,
    anchor="nw",
    text="Welcome Back !",
    fill="#000000",
    font=("Inter Bold", 37 * -1)
)

canvas.create_text(
    671.0,
    118.0,
    anchor="nw",
    text="Login to continue",
    fill="#838383",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    661.0,
    511.0,
    anchor="nw",
    text="Forgot Password?",
    fill="#838383",
    font=("Inter Bold", 19 * -1)
)

canvas.create_text(
    638.0,
    605.0,
    anchor="nw",
    text="New User?",
    fill="#838383",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    758.0,
    605.0,
    anchor="nw",
    text="Register",
    fill="#6C63FF",
    font=("Inter Bold", 22 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    748.5,
    237.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=622.0,
    y=210.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    603.0,
    183.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    748.5,
    356.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_2.place(
    x=622.0,
    y=329.0,
    width=253.0,
    height=52.0,
)

canvas.create_text(
    603.0,
    302.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=644.0,
    y=436.0,
    width=201.0,
    height=56.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    291.0,
    177.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    276.0,
    476.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    49.0,
    36.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
