from tkinter import *
from tkinter import messagebox as mb
from random import randint as randomize
from time import sleep

lower, higher = 0, 1000
number = 0
tk = Tk()
tk.title("Guess Integer")
tk.geometry("400x200")

#upon pressing the "Lower" button
def toohigh():
    global higher, lower
    higher = round((lower+higher)/2)
    startbot()

#upon pressing the "Higher" button
def toolow():
    global higher, lower
    lower = round((lower+higher)/2)
    startbot()

#upon pressing the "This one" button
def celebrate():
    mb.showinfo("I won", "Huh bitch, didn't expect me to win?")
    if mb.askyesno("Play again?", "Shall we start a new game?"):
        startgame()
    else:
        mb.showinfo("Bye then", "Goodbye, loser")
        tk.destroy()

#method for bot's guess
#creates a dialog with the guessed number and three buttons(Lower, Higher and This one) for the user to reply to the guess
def botguess():
    global lower, higher
    tk.title("Bot guessed")
    guessednum = Label(tk, text = str(round((lower+higher)/2)))
    guessednum.pack()
    info = Label(tk, text = "My nuber is: ")
    info.pack()
    low = Button(tk, text = "Lower", command = toohigh)
    low.pack()
    high = Button(tk, text = "Higher", command = toolow)
    high.pack()
    exact = Button(tk, text = "This one", command = celebrate)
    exact.pack()

#method for after user's guess (compares input to the pregenerated number)
def guess(guessednumber):
    global number
    try:
        if int(guessednumber) == number:
            mb.showinfo("Exactly", "That's the number I was thinking")
            if mb.askyesno("Play again?", "Shall we start a new game?"):
                startgame()
            else:
                mb.showinfo("Bye then", "Goodbye, have a nice life")
                tk.destroy()
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
            tk.destroy()
    else:
        pass

#when bot is supposed to guess
def startbot():
    for child in tk.winfo_children():
        child.destroy()
    tk.title("Bot thinking...")
    sleep(0.6)
    botguess()
    
#when player wants to guess
def startplayer():
    global number
    number = randomize(1, 1000)
    label = Label(tk, text = "Enter a number (integer) below:")
    label.pack()
    guessednum = Entry(tk)
    guessednum.bind("<Return>", lambda a: guess(guessednum.get()))
    guessednum.pack()
    guessbutton = Button(tk, text = "Submit guess", command = lambda: guess(guessednum.get()))
    guessbutton.pack()
    giveupbutton = Button(tk, text = "Give up", command = giveup)
    giveupbutton.pack()
    guessednum.focus_force()

#what happens after the launch and in case of restart (clearing the window and setting guesser)
def startgame():
    for child in tk.winfo_children():
        child.destroy()
    if mb.askyesno("Who's gonna guess?", "Will you be the guesser?"):
        startplayer()
    else:
        mb.showinfo("Think of a number", "Think of a number, when you have it, press ok")
        startbot()

startgame()
