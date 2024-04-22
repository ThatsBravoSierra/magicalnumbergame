from tkinter import *

from answer_gen import *

with open("Colours.txt", "r") as file:
    colours = file.read()
    exec(colours)

# Window Parameters
root = Tk()
root.title("Robert's Fantastic Magical Number Game")
root.configure(bg=darkgrey)
root.resizable(True, True)

# Version
version = "Version 0"
versiontext = Label(root, text=version, fg=white, bg=darkgrey)
versiontext.place(x=0, y=0)

# Top label
textlabel = Label(root, text="Welcome! This game is tough! Think you can win?", fg=red, bg=darkgrey)
textlabel.grid(row=0, column=1)

# Guess box
guesslabel = Label(root, text="Take your guess", fg=blue, bg=darkgrey)
guesslabel.grid(row=1, column=0)

# Guess drop down
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbersdrop = StringVar()
numbersdrop.set(numbers[0])
numbersinput = OptionMenu(root, numbersdrop, *numbers)
numbersinput.config(bg=darkgrey, fg=white)
numbersinput["menu"].config(fg=white, bg=darkgrey)
numbersinput.grid(row=2, column=0)

# Guess button
guessbutton = Button(root, text="GUESS", padx=10, pady=10, command=answer, fg=white, bg=green)
guessbutton.grid(row=2, column=1)

# Answer Display
answerlabel = Label(root, text="Answer", fg=blue, bg=darkgrey)
answerlabel.grid(row=1, column=2)

finalanswer_var = StringVar()
finalanswer_var.set(finalanswer)
finalanswerlabel = Label(root, text=finalanswer_var, fg=blue, bg=darkgrey)
finalanswerlabel.grid(row=2, column=2)

root.mainloop()
