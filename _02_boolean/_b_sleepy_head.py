"""
Use boolean variables to control program logic between two different code
paths.
"""
from tkinter import simpledialog, messagebox
import turtle
from turtle import Turtle


if __name__ == '__main__':



    is_weekend = False
    day_week =  simpledialog.askstring(None,"What day is it?")

    #  1. Use a boolean variable to indicate if it is the weekend.
    if day_week == "Saturday" or day_week == "Sunday":
        is_weekend = True
        messagebox.showinfo(None,"Have a great Weekend!")
    else:
        messagebox.showinfo(None,'almost there!')

    if is_weekend:
        test_quest = simpledialog.askstring(None,"did you pass all your test?")
        if test_quest == "yes":
            messagebox.showinfo(None,"Great Job!")
        else:
            messagebox.showinfo(None,"Study more! ")
    if is_weekend:
        game_on = simpledialog.askstring(None, "Is the game on?")

        if game_on == "yes":
            messagebox.showinfo(None,"Have fun!")
        else:
            messagebox.showinfo(None,"Can't Wait!")

    if is_weekend:
        red_color= simpledialog.showinfo(None,"Should the shape be red?")

        if red_color == "yes":
            window = turtle.Screen()
            window.bgcolor('white')

    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    pass
