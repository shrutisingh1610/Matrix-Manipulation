import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage







OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame4")



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

tranpose_A = eval(result[2])
tranpose_B = eval(result[3])

# Close the cursor and the connection
cursor.close()
conn.close()




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def history():
    os.system("python history.py")
def back():
    os.system("python dashboard.py")

window = Tk()

window.title("Transpose")
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
    328.0,
    122.0,
    anchor="nw",
    text="TRANSPOSE",
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
    110.0,
    232.0,
    anchor="nw",
    text="Transpose of Matrix A ",
    fill="#838383",
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
    110.0,
    317.0,
    190.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix A1
canvas.create_text(
    129.0,
    323.0,
    anchor="nw",
    text=tranpose_A[0][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    214.0,
    317.0,
    294.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix A2
canvas.create_text(
    233.0,
    323.0,
    anchor="nw",
    text=tranpose_A[0][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)
canvas.create_rectangle(
    318.0,
    317.0,
    398.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix A3
canvas.create_text(
    337.0,
    323.0,
    anchor="nw",
    text=tranpose_A[0][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)


canvas.create_rectangle(
    110.0,
    414.0,
    190.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix A4
canvas.create_text(
    129.0,
    420.0,
    anchor="nw",
    text=tranpose_A[1][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    214.0,
    414.0,
    294.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix A5
canvas.create_text(
    233.0,
    420.0,
    anchor="nw",
    text=tranpose_A[1][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    318.0,
    414.0,
    398.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix A6
canvas.create_text(
    337.0,
    420.0,
    anchor="nw",
    text=tranpose_A[1][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    110.0,
    511.0,
    190.0,
    591.0,
    fill="#6C25FF",
    outline="")
# Matrix A7
canvas.create_text(
    129.0,
    517.0,
    anchor="nw",
    text=tranpose_A[2][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    214.0,
    510.0,
    294.0,
    590.0,
    fill="#6C25FF",
    outline="")
# Matrix A8
canvas.create_text(
    233.0,
    516.0,
    anchor="nw",
    text=tranpose_A[2][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)



canvas.create_rectangle(
    318.0,
    510.0,
    398.0,
    590.0,
    fill="#6C25FF",
    outline="")
# Matrix A9
canvas.create_text(
    337.0,
    516.0,
    anchor="nw",
    text=tranpose_A[2][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)




canvas.create_text(
    596.0,
    232.0,
    anchor="nw",
    text="Transpose of Matrix B",
    fill="#838383",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    596.0,
    317.0,
    676.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix B1
canvas.create_text(
    615.0,
    323.0,
    anchor="nw",
    text=tranpose_B[0][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    700.0,
    317.0,
    780.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix B2 
canvas.create_text(
    719.0,
    323.0,
    anchor="nw",
    text=tranpose_B[0][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    804.0,
    317.0,
    884.0,
    397.0,
    fill="#6C25FF",
    outline="")
# Matrix B3
canvas.create_text(
    823.0,
    323.0,
    anchor="nw",
    text=tranpose_B[0][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    596.0,
    414.0,
    676.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix B4
canvas.create_text(
    615.0,
    420.0,
    anchor="nw",
    text=tranpose_B[1][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)


canvas.create_rectangle(
    700.0,
    414.0,
    780.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix B5
canvas.create_text(
    719.0,
    420.0,
    anchor="nw",
    text=tranpose_B[1][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    804.0,
    414.0,
    884.0,
    494.0,
    fill="#6C25FF",
    outline="")
# Matrix B6
canvas.create_text(
    823.0,
    420.0,
    anchor="nw",
    text=tranpose_B[1][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    596.0,
    511.0,
    676.0,
    591.0,
    fill="#6C25FF",
    outline="")
# Matrix B7
canvas.create_text(
    615.0,
    517.0,
    anchor="nw",
    text=tranpose_B[2][0],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)

canvas.create_rectangle(
    700.0,
    510.0,
    780.0,
    590.0,
    fill="#6C25FF",
    outline="")
# Matrix B8
canvas.create_text(
    719.0,
    516.0,
    anchor="nw",
    text=tranpose_B[2][1],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)


canvas.create_rectangle(
    804.0,
    510.0,
    884.0,
    590.0,
    fill="#6C25FF",
    outline="")
# Matrix B9
canvas.create_text(
    823.0,
    516.0,
    anchor="nw",
    text=tranpose_B[2][2],
    fill="#FFFFFF",
    font=("Inter Bold", 25 * -1)
)


window.resizable(False, False)
window.mainloop()
