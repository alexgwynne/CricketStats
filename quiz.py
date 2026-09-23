#Cricket Rules Quiz with graphical interface
#By Alex Gwynne
#Comments are above what they comment on

#This 'tkinter' code is what allows the python program to appear in a graphical interface rather than the terminal
import tkinter as tk
from tkinter import ttk, messagebox

quizquestions = [

]

#'root' code is for the main window that the graphical interface appears in
root = tk.Tk()
root.title("Cricket Rules Quiz")
root.geometry("500x400")

#Required at the end of the python program for it to work
root.mainloop()