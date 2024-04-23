# from answer_gen import *

import random

from tkinter import *

with open("Colours.txt", "r") as file:
    colours = file.read()
    exec(colours)

# Window Parameters
root = Tk()
root.title("Robert's Fantastic Magical Number Game")
root.configure(bg=darkgrey)
root.resizable(True, True)

# Version
version = "Version 1"
versiontext = Label(root, text=version, fg=white, bg=darkgrey)
versiontext.place(x=0, y=0)

# Top label
textlabel = Label(root, text="------------World's Best Roguelike------------", fg=red, bg=darkgrey)
textlabel.grid(row=0, column=1)

# Guess box
guesslabel = Label(root, text="Take your guess", fg=blue, bg=darkgrey)
guesslabel.grid(row=1, column=0)

# Guess drop down
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
numbersdrop = StringVar()
numbersdrop.set(numbers[0])
numbersinput = OptionMenu(root, numbersdrop, *numbers)
numbersinput.config(bg=darkgrey, fg=white)
numbersinput["menu"].config(fg=white, bg=darkgrey)
numbersinput.grid(row=2, column=0)
guess = numbersdrop.get()

# answer
finalanswer = "???"
finalanswer_var = StringVar()
finalanswer_var.set(finalanswer)

result = ""
result_var = StringVar()
result_var.set(result)

points_int = 0
points_var = StringVar()
points_var.set(str(points_int))


def reset_game():
    global finalanswer
    global guess
    global result_var
    global points_int
    global points_var

    finalanswer = "0"
    guess = "0"
    result_var.set("")
    points_int = 0
    points_var.set("0")
    guessbutton.grid(row=2, column=1)
    retrybutton.grid_forget()


def answer():
    global finalanswer
    global guess
    global result_var
    global points_int
    global points_var
    guess = numbersdrop.get()
    hold = finalanswer
    while hold == finalanswer:
        finalanswer = random.randint(1, 10)

    finalanswer_str = str(finalanswer)
    finalanswer_var.set(finalanswer_str)
    if guess == finalanswer_str:
        result_var.set("correct")
        points_int = + 1
        points_var.set(str(points_int))
    else:
        result_var.set("incorrect")
        guessbutton.grid_forget()
        retrybutton.grid(row=2, column=1)


retrybutton = Button(root, text="Retry", padx=10, pady=10, command=reset_game, fg=red, bg=grey)

# Guess button
guessbutton = Button(root, text="GUESS", padx=10, pady=10, command=answer, fg=white, bg=green)
guessbutton.grid(row=2, column=1)

# Answer Display
answerlabel = Label(root, text="Answer", fg=blue, bg=darkgrey)
answerlabel.grid(row=1, column=2)

finalanswerlabel = Label(root, textvariable=finalanswer_var, fg=blue, bg=darkgrey)
finalanswerlabel.grid(row=2, column=2)

# Results
resultlabel = Label(root, text="Result", fg=blue, bg=darkgrey)
resultlabel.grid(row=3, column=1)

resulttext = Label(root, textvariable=result_var, fg=blue, bg=darkgrey)
resulttext.grid(row=4, column=1)

# points
pointslabel = Label(root, text="Points", fg=blue, bg=darkgrey)
pointslabel.grid(row=5, column=1)

pointstext = Label(root, textvariable=points_var, fg=blue, bg=darkgrey)
pointstext.grid(row=6, column=1)

root.mainloop()
