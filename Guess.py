from tkinter import *
from tkinter import messagebox as mb
from random import randint as randomize

def guess():
    try:
        if int(gn.get()) == number:
            mb.showinfo("Exactly", "That's the number I was thinking")
        elif gn.get() > number:
            mb.showinfo("Lower", "My number is lower than " + str(gn.get()))
        else:
            mb.showinfo("Bigger", "Oh, I'm thinking of a bigger number")
    except ValueError:
        mb.showwarning("Integers only!", "IDC if you entered a float or a string, gimme an integer")
    except:
        mb.showerror("Error", "Wild Error appeared (just report to the creator)")

