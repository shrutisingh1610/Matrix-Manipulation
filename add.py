import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def history():
    os.system("python history.py")
def back():
    os.system("python dashboard.py")

import pymysql

# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='12345678', db='MPR')

# Create a cursor object
cursor = conn.cursor()

# Define the query to fetch the latest record
query = "SELECT * FROM M_DATA_3 ORDER BY created_at DESC LIMIT 1"

# Execute the query
cursor.execute(query)

# Fetch the result
result = cursor.fetchone()

# Print the result
print(eval(result[2]))
# Close the cursor and the connection
cursor.close()
conn.close()


result = eval(result[2])

window = Tk()

window.title("Add")
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
    434.0,
    123.0,
    anchor="nw",
    text="ADD",
    fill="#4C4C4C",
    font=("Inter Bold", 55 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    789.0,
    43.0,
    image=image_image_3
)

canvas.create_text(
    295.0,
    216.0,
    anchor="nw",
    text="Addition of Matrix A and Matrix B",
    fill="#825253",
    font=("Inter Bold", 25 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=history,
    relief="flat"
)
button_1.place(
    x=612.0,
    y=20.0,
    width=131.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_2.place(
    x=24.0,
    y=99.0,
    width=131.0,
    height=47.0
)

canvas.create_rectangle(
    356.0,
    310.0,
    436.0,
    390.0,
    fill="#6C63FF",
    outline="")
# 1
canvas.create_text(
    363.0,
    315.0,
    anchor="nw",
    text=result[0][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    460.0,
    310.0,
    540.0,
    390.0,
    fill="#6C63FF",
    outline="")
# 2
canvas.create_text(
    464.0,
    313.0,
    anchor="nw",
    text=result[0][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    564.0,
    310.0,
    644.0,
    390.0,
    fill="#6C63FF",
    outline="")
# 3
canvas.create_text(
    568.0,
    313.0,
    anchor="nw",
    text=result[0][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    356.0,
    407.0,
    436.0,
    487.0,
    fill="#6C63FF",
    outline="")
# 4
canvas.create_text(
    360.0,
    410.0,
    anchor="nw",
    text=result [1][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    460.0,
    407.0,
    540.0,
    487.0,
    fill="#6C63FF",
    outline="")
# 5
canvas.create_text(
    464.0,
    410.0,
    anchor="nw",
    text=result[1][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    564.0,
    407.0,
    644.0,
    487.0,
    fill="#6C63FF",
    outline="")
# 6
canvas.create_text(
    568.0,
    410.0,
    anchor="nw",
    text=result[1][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    356.0,
    504.0,
    436.0,
    584.0,
    fill="#6C63FF",
    outline="")
# 7
canvas.create_text(
    360.0,
    507.0,
    anchor="nw",
    text=result[2][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    460.0,
    503.0,
    540.0,
    583.0,
    fill="#6C63FF",
    outline="")
# 8
canvas.create_text(
    464.0,
    506.0,
    anchor="nw",
    text=result[2][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    564.0,
    503.0,
    644.0,
    583.0,
    fill="#6C63FF",
    outline="")
# 9
canvas.create_text(
    568.0,
    506.0,
    anchor="nw",
    text=result[2][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)


window.resizable(False, False)
window.mainloop()
