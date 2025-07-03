import tkinter
from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("570x600")
root.resizable(False,False)
root.config(bg="blue")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation!="":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
        label_result.config(text=result)

label_result = Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()