from tkinter import *
from tkinter import messagebox
from os import system

root = Tk()
root.title("AminoRep Manager")
root.geometry("1366x760")
root.config(background="gray17")

def repFarmCommand():
    messagebox.showinfo("Done!", "Script is started, check terminal!")
    system("python main.py")
    print("200")

def creditsScript():
    system("start credits.txt")

repButton = Button(root, text="Rep farm start(script in terminal)", command=repFarmCommand, pady=10, background="gray17", fg="lime")
repButton.pack()
creditButton = Button(root, text="Credits", command=creditsScript, pady=10, background="gray17", fg="lime")
creditButton.pack()

root.mainloop()