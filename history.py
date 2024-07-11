import os
from pathlib import Path
from random import choice
import tkinter as tk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import CENTER, W, Tk, ttk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame7")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back():
    os.system("python dashboard.py")

window = Tk()

window.title("History")
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
    97.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    407.0,
    image=image_image_2
)

canvas.create_text(
    824.0,
    35.0,
    anchor="nw",
    text="Rishabh Sinha",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    400.0,
    95.0,
    anchor="nw",
    text="History",
    fill="#4C4C4C",
    font=("Inter Bold", 55 * -1)
)

style = ttk.Style(window)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#404275", foreground="white")


# table data 
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
type = ['Addition', 'Transpose', 'Addition', 'Multiplication', 'Inverse', 'Addition', 'Inverse', 'Addition']

# table 
table = ttk.Treeview(window, columns = ('first', 'email', 'type', 'result'), show = 'headings')
table.heading('first', text = 'Name')
table.heading('email', text = 'Email')
table.heading('type', text = 'Type')
table.heading('result', text = 'Result')
table.pack(fill = 'both', expand = True ,side="bottom", padx=80, pady=(180,4))

# table = ttk.Style()
# table.configure('table', foreground='red')

for i in range(100):
	first = choice(first_names)
	email = f'{first[0]}@email.com'
	types = choice(type)
	data = (first, email, types, email)
	table.insert(parent = '', index = 0, values = data)

# # events
# def item_select(_):
# 	print(table.selection())
# 	for i in table.selection():
# 		print(table.item(i)['values'])
# 	# table.item(table.selection())

# def delete_items(_):
# 	print('delete')
# 	for i in table.selection():
# 		table.delete(i)

# table.bind('<<TreeviewSelect>>', item_select)
# table.bind('<Delete>', delete_items)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    789.0,
    43.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_1.place(
    x=24.0,
    y=99.0,
    width=131.0,
    height=47.0
)

window.resizable(False, False)
window.mainloop()
