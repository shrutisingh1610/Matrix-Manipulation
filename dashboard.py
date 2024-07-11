import os
from pathlib import Path
import pymysql
import numpy as np

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def add():
    A = entry_1.get().split(",")
    B = entry_2.get().split(",")
    matrix_A = [int(x) for x in A]
    matrix_B = [int(x) for x in B]
    
    matrix_A = np.reshape(matrix_A, (3, 3))
    matrix_B = np.reshape(matrix_B, (3, 3))
    print(matrix_A)
    # if len(A) == len(B) and len(A[0]) == len(B[0]):
    # C = [[0 for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]
    matrix_C=[]

    for i in range(len(matrix_A)):
        matrix_C.append([])
        for j in range(len(matrix_A)):
           
            matrix_C[i].append(matrix_A[i][j] + matrix_B[i][j])
    print(matrix_C)
    con = pymysql.connect(host="localhost",user="root",password="12345678",database="MPR")
    cur = con.cursor()
    cur.execute("insert into M_DATA_3(matrix1,matrix2,result1,result2,optype) values(%s,%s,%s,%s,%s)",
					(
					str(matrix_A),
					str(matrix_B),
					str(matrix_C),
                    "",
                    "Addition",
					))
    con.commit()
    con.close()
    os.system("python add.py")
    # else:
    #     return "Matrices have different shapes."
def multiply():
    A = entry_1.get().split(",")
    B = entry_2.get().split(",")
    matrix_A = [int(x) for x in A]
    matrix_B = [int(x) for x in B]
    
    matrix_A = np.reshape(matrix_A, (3, 3))
    matrix_B = np.reshape(matrix_B, (3, 3))
    print(matrix_A)
    # if len(A) == len(B) and len(A[0]) == len(B[0]):
    # C = [[0 for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]
    matrix_C=[]

    for i in range(len(matrix_A)):
        matrix_C.append([])
        for j in range(len(matrix_A)):
           
            matrix_C[i].append(matrix_A[i][j] * matrix_B[i][j])
    print(matrix_C)
    con = pymysql.connect(host="localhost",user="root",password="12345678",database="MPR")
    cur = con.cursor()
    cur.execute("insert into M_DATA_3(matrix1,matrix2,result1,result2,optype) values(%s,%s,%s,%s,%s)",
					(
					str(matrix_A),
					str(matrix_B),
					str(matrix_C),
                    "",
                    "Multiplication",
					))
    con.commit()
    con.close()


    os.system("python multiply.py")


def inverse():  

    A = entry_1.get().split(",")
    B = entry_2.get().split(",")
    matrix_A = [int(x) for x in A]
    matrix_B = [int(x) for x in B]
    
    matrix_A = np.reshape(matrix_A, (3, 3))
    matrix_B = np.reshape(matrix_B, (3, 3))
    print(matrix_A)
    result1=np.linalg.inv(matrix_A)
    result2=np.linalg.inv(matrix_B)

    result1 = [[float(x) for x in row] for row in result1]
    result2 = [[float(x) for x in row] for row in result2]

    result1 = [[format(x, '.2f') for x in row] for row in result1]
    result2 = [[format(x, '.2f') for x in row] for row in result2]


    print("result1:",result1)
    print("result2:",result2)
    
    con = pymysql.connect(host="localhost",user="root",password="12345678",database="MPR")
    cur = con.cursor()
    cur.execute("insert into M_DATA_3(matrix1,matrix2,result1,result2,optype) values(%s,%s,%s,%s,%s)",
					(
					str(matrix_A),
					str(matrix_B),
                    str(result1),
                    str(result2),
                    "Inverse",
					))
    con.commit()
    con.close()



    os.system("python inverse.py")


def transpose():
    A = entry_1.get().split(",")
    B = entry_2.get().split(",")
    matrix_A = [int(x) for x in A]
    matrix_B = [int(x) for x in B]
    
    matrix_A = np.reshape(matrix_A, (3, 3))
    matrix_B = np.reshape(matrix_B, (3, 3))
    print(matrix_A)

    # Tanspose of first Matix 
    result1=[[0 for _ in range(len(matrix_A))]for i in range(len(matrix_A))]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[0])):
            result1[j][i] = matrix_A[i][j]
    print("Transpose of matrix A")

    # Tanspose of second Matix 
    result2=[[0 for _ in range(len(matrix_B))]for i in range(len(matrix_B))]
    for i in range(len(matrix_B)):
        for j in range(len(matrix_B[0])):
            result2[j][i] = matrix_B[i][j]
    print("Transpose of matrix B")

    con = pymysql.connect(host="localhost",user="root",password="12345678",database="MPR")
    cur = con.cursor()
    cur.execute("insert into M_DATA_3(matrix1,matrix2,result1,result2,optype) values(%s,%s,%s,%s,%s)",
					(
					str(matrix_A),
					str(matrix_B),
					str(result1),
                    str(result2),
                    "Transpose",
					))
    con.commit()
    con.close()

    os.system("python transpose.py")


def history():
    os.system("python history.py")








def multiply():
    print("BUtton 3 is clicked")
    print("In multiply")
    A = entry_1.get().split(",")
    B = entry_2.get().split(",")
    matrix_A = [int(x) for x in A]
    matrix_B = [int(x) for x in B]
    
    matrix_A = np.reshape(matrix_A, (3, 3))
    matrix_B = np.reshape(matrix_B, (3, 3))
    print(matrix_A)
    # if len(A) == len(B) and len(A[0]) == len(B[0]):
    # C = [[0 for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]
    matrix_C=[]

    for i in range(len(matrix_A)):
        matrix_C.append([])
        for j in range(len(matrix_A)):
           
            matrix_C[i].append(matrix_A[i][j] * matrix_B[i][j])
    print(matrix_C)
    con = pymysql.connect(host="localhost",user="root",password="12345678",database="MPR")
    cur = con.cursor()
    cur.execute("insert into M_DATA_3(matrix1,matrix2,result1,result2,optype) values(%s,%s,%s,%s,%s)",
					(
					str(matrix_A),
					str(matrix_B),
					str(matrix_C),
                    "",
                    "Multiplication",
					))
    con.commit()
    con.close()
    os.system("python multiply.py")
    # else:
    #     return "Matrices have different shapes."



window = Tk()

window.title("Dashboard")
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
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    97.0,
    43.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    500.0,
    407.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    229.0,
    318.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=59.0,
    y=268.0,
    width=340.0,
    height=98.0
)

canvas.create_text(
    37.0,
    241.0,
    anchor="nw",
    text="Matrix A:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    565.0,
    376.0,
    anchor="nw",
    text="Add",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
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
    294.0,
    123.0,
    anchor="nw",
    text="Play with Matrix !",
    fill="#4C4C4C",
    font=("Inter Bold", 55 * -1)
)

canvas.create_text(
    549.0,
    586.0,
    anchor="nw",
    text="Multiply",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    806.0,
    376.0,
    anchor="nw",
    text="Inverse",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    789.0,
    586.0,
    anchor="nw",
    text="Transpose",
    fill="#4C4C4C",
    font=("Inter Bold", 20 * -1)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    229.0,
    530.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=59.0,
    y=480.0,
    width=340.0,
    height=98.0
)

canvas.create_text(
    37.0,
    453.0,
    anchor="nw",
    text="Matrix B:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=inverse,
    relief="flat"
)
button_1.place(
    x=743.0,
    y=268.0,
    width=200.0,
    height=100.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=transpose,
    relief="flat"
)
button_2.place(
    x=743.0,
    y=479.0,
    width=200.0,
    height=100.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=multiply,
    relief="flat"
)
button_3.place(
    x=486.0,
    y=480.0,
    width=200.0,
    height=100.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= add,
    relief="flat"
)
button_4.place(
    x=486.0,
    y=268.0,
    width=200.0,
    height=100.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    789.0,
    43.0,
    image=image_image_3
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=history,
    relief="flat"
)
button_5.place(
    x=612.0,
    y=20.0,
    width=131.0,
    height=47.0
)
window.resizable(False, False)
window.mainloop()