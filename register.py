import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame8")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def register():
    os.system("python dashboard.py")

window = Tk()

window.title("Registration")
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
    679.0,
    26.0,
    anchor="nw",
    text="Register",
    fill="#000000",
    font=("Inter Bold", 37 * -1)
)

canvas.create_text(
    577.0,
    651.0,
    anchor="nw",
    text="Already Registered?",
    fill="#838383",
    font=("Inter Bold", 22 * -1)
)

canvas.create_text(
    808.0,
    651.0,
    anchor="nw",
    text="Login",
    fill="#6C63FF",
    font=("Inter Bold", 22 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    744.5,
    150.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=618.0,
    y=123.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    599.0,
    96.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    744.5,
    245.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=618.0,
    y=218.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    599.0,
    191.0,
    anchor="nw",
    text="Email:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    744.5,
    340.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=618.0,
    y=313.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    599.0,
    286.0,
    anchor="nw",
    text="Username:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    744.5,
    436.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_4.place(
    x=618.0,
    y=409.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    599.0,
    382.0,
    anchor="nw",
    text="Password:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    744.5,
    527.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EBEAFF",
    fg="#000716",
    highlightthickness=0,
    show="*"
)
entry_5.place(
    x=618.0,
    y=500.0,
    width=253.0,
    height=52.0
)

canvas.create_text(
    599.0,
    473.0,
    anchor="nw",
    text="Confirm Password:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=register,
    relief="flat"
)
button_1.place(
    x=644.0,
    y=580.0,
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
    49.0,
    36.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    311.0,
    492.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
