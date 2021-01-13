from tkinter import *
from tkinter import messagebox as mb
from random import randint as randomize
from time import sleep

lower, higher = 0, 1000
number = 0
tk = Tk()
tk.title("Guess Integer")

#upon pressing the "Lower" button
def toohigh():
    dialog.destroy()
    global higher, lower
    higher = round((lower+higher)/2)
    sleep(1)
    botguess()

#upon pressing the "Higher" button
def toolow():
    dialog.destroy()
    global higher, lower
    lower = round((lower+higher)/2)
    sleep(1)
    botguess()

#upon pressing the "This one" button
def celebrate():
    dialog.destroy()
    mb.showinfo("I won", "Huh bitch, didn't expect me to win?")
    if mb.askyesno("Play again?", "Shall we start a new game?"):
        startgame()
    else:
        mb.showinfo("Bye then", "Goodbye, loser")

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

#method for after user's guess (compares input to the pregenerated number)
def guess(guessednumber):
    global number
    try:
        if int(guessednumber) == number:
            mb.showinfo("Exactly", "That's the number I was thinking")
        elif int(guessednumber) > number:
            mb.showinfo("Lower", "My number is lower than " + str(guessednumber))
        else:
            mb.showinfo("Bigger", "Oh, I'm thinking of a higher number than " + str(guessednumber))
    except ValueError:
        mb.showwarning("Integers only!", "IDC if you entered a float or a string, gimme an integer")
    except:
        mb.showerror("Error", "Wild Error appeared (just report to the creator)")

#when player clicks the give up button
def giveup():
    if mb.askyesno("Give up?", "Do you really wanna give up?"):
        if mb.askyesno("Play again?", "Shall we start a new game?"):
            startgame()
        else:
            mb.showinfo("Bye then", "Goodbye, loser")
    else:
        pass

#when player wants to guess
def startplayer():
    global number
    number = randomize(1, 1000)
    label = Label(tk, text = "Enter a number (integer) below:")
    label.pack()
    guessednum = Entry(tk)
    guessednum.pack()
    guessbutton = Button(tk, text = "Submit guess", command = lambda: guess(guessednum.get()))
    guessbutton.pack()
    giveupbutton = Button(tk, text = "Give up", command = giveup)
    giveupbutton.pack()
    guessednum.focus_force()

#what happens after the launch and in case of restart
def startgame():
    if mb.askyesno("Who's gonna guess?", "Will you be the guesser?"):
        startplayer()
    else:
        mb.showinfo("Think of a number", "Think of a number, when you have it, press ok")
        sleep(1)
        botguess()

startgame()
tk.mainloop()
