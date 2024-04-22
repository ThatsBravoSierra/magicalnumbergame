import random

from tkinter import *

finalanswer = 0
finalanswer_var = 0


def answer():
    global finalanswer
    finalanswer = random.randint(1, 10)
    finalanswer_var.set(finalanswer)
    print(finalanswer)
