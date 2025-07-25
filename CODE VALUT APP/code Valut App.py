from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()
    if password =="1234":
        screen2 = Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.config(bg="blue")

        message = text1.get("1.0",END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="grey").place(x=10,y=0)
        text2 = Text(screen2,font="Roboto 10",fg="white",bg="grey",relief=GROOVE,wrap="word",bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)
    elif password == "":
        messagebox.showerror("ENCRYPTION","Input Password")
    elif password == "1234":
        messagebox.showerror("ENCRYPTION","Invalid Password")

def encrypt():
    password = code.get()
    if password =="1234":
        screen1 = Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.config(bg="blue")

        message = text1.get("1.0",END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="grey").place(x=10,y=0)
        text2 = Text(screen1,font="Roboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
    elif password =="":
        messagebox.showerror("ENCRYPTION","Input Password")
    elif password != "1234":
        messagebox.showerror("ENCRYPTION","Invalid Password")

def main_screen():
    global screen
    global code 
    global text1

    screen = Tk()
    screen.geometry("400x300")
    # screen.iconbitmap(r'C:\coding in different different languages\PYTHON\ENCRYPTION AND DECRYPTION\keys.ico')  # Commented out to avoid path errors
    screen.title("Code Valut App")

    def reset():
        code.set("")
        text1.delete("1.0", END)


    Label(text="Enter The Text For Encryption and Decryption",fg="black",font=("Cosmic Sans Ms",12)).place(x=10,y=10)
    text1 = Text(font="Roboto 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text = "Enter Secret Key For Encryption and Decryption",fg="black",font=("Cosmic Sans Ms",11)).place(x=10,y=170)
    code = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height=2,width=15,bg="black",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height=2,width=15,bg="black",fg="white",bd=0,command=decrypt).place(x=140,y=250)
    Button(text="RESET",height=2,width=15,bg="black",fg="white",bd=0,command=reset).place(x=270,y=250)

    screen.mainloop()

main_screen()

        
