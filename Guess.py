from tkinter import *
from tkinter import messagebox as mb
from random import randint as randomize
from time import sleep

#method for after user's guess (compares input to the pregenerated number)
def guess():
    try:
        if int(gn.get()) == number:
            mb.showinfo("Exactly", "That's the number I was thinking")
        elif gn.get() > number:
            mb.showinfo("Lower", "My number is lower than " + str(gn.get()))
        else:
            mb.showinfo("Bigger", "Oh, I'm thinking of a higher number than " + str(gn.get()))
    except ValueError:
        mb.showwarning("Integers only!", "IDC if you entered a float or a string, gimme an integer")
    except:
        mb.showerror("Error", "Wild Error appeared (just report to the creator)")

#method for bot's guess
#creates a dialog with the guessed number and three buttons(Lower, Higher and This one) for the user to reply to the guess
def botguess():
    global lower, higher
    dialog = Tk()
    dialog.title("Bot guessed")
    guessednum = Label(dialog, text = str(round((lower+higher)/2)))
    guessednum.pack()
    info = Label(tk, text = "My nuber is: ")
    info.pack()
    lower = Button(dialog, text = "Lower", command = toohigh)
    lower.pack()
    higher = Button(dialog, text = "Higher", command = toolow)
    higher.pack()
    exact = Button(dialog, text = "This one", command = celebrate)
    exact.pack()
    dialog.mainloop()
