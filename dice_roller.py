import tkinter as tk
from random import randint

# Dice roller program that returns the outcome of an n-sided die rolled x times.

# ---WINDOW_SETTINGS---
window = tk.Tk()
window.title("Dice Roller")
window.geometry("350x350")
window.iconbitmap('c:/users/shawn/pycharmprojects/savings_calc/tk_dice_roller/dice_roller.ico')


# ---FUNCTIONS---

def enter_sides():
    """Accept the number of sides on a dice"""
    return int(sides_entry.get())


def enter_rolls():
    """Accept the number of rolls on a dice"""
    return int(times_entry.get())


def roll_die(sides):
    """Roll a die x number of times"""
    outcomes = []
    for i in range(enter_rolls()):
        roll = randint(1, sides)
        outcomes.append(roll)
    return outcomes

def clear_rolls():
    """Clear the outcome window"""
    displays = [sixes_display, fives_display, fours_display, threes_display, twos_display, ones_display]
    for display in displays:
        display.delete("1.0", tk.END)


def reroll(number): #
    """Function for rerolling dice of a certain type, ie, reroll 6s"""
    six_list = []
    displays = [sixes_display, fives_display, fours_display, threes_display, twos_display, ones_display]
    sixes = displays[number].get("1.0", tk.END)
    for i in sixes:
        if i != "\n" and i != " ":
            six_list.append(i)
    displays[number].delete("1.0", tk.END)
    for i in six_list:
        reroll = str(randint(1, enter_sides())) + " "
        displays[number].insert(tk.END, reroll)


def display_outcome():
    """Display the results of the die rolls"""
    clear_rolls()
    outcome = roll_die(enter_sides())
    sixes = []
    fives = []
    fours = []
    threes = []
    twos = []
    ones = []

    # Outcome of rolls
    for i in outcome:
        if i == 6:
            sixes.append(i)
        elif i == 5:
            fives.append(i)
        elif i == 4:
            fours.append(i)
        elif i == 3:
            threes.append(i)
        elif i == 2:
            twos.append(i)
        elif i == 1:
            ones.append(i)
    # Sixes rolled
    if len(sixes) != 0:
        sixes_display.insert(tk.END, sixes)
    # Fives rolled
    if len(fives) != 0:
        fives_display.insert(tk.END, fives)
    # Fours rolled
    if len(fours) != 0:
        fours_display.insert(tk.END, fours)
    # Threes rolled
    if len(threes) != 0:
        threes_display.insert(tk.END, threes)
    # Twos rolled
    if len(twos) != 0:
        twos_display.insert(tk.END, twos)
    # Ones rolled
    if len(ones) != 0:
        ones_display.insert(tk.END, ones)
    return outcome


# ---LABELS---
explain_label = tk.Label(window, text="Dice Roller Simulator", font=(16)).grid(row=0, columnspan=2)
dice_sides = tk.Label(window, text="Enter how many sides on the die").grid(row=1, sticky=tk.W)
times_rolled = tk.Label(window, text="Enter how many times you want to roll the die").grid(row=4, sticky=tk.W)


# ---ENTRY WINDOWS---
sides_entry = tk.Entry()
sides_entry.grid(row=3, column=0)
times_entry = tk.Entry()
times_entry.grid(row=5, column=0)


# ---TEXT FIELDS---
sixes_display = tk.Text(window, height=1, width=15)
sixes_display.grid(row=9, column=0)
fives_display = tk.Text(window, height=1, width=15)
fives_display.grid(row=10, column=0)
fours_display = tk.Text(window, height=1, width=15)
fours_display.grid(row=11, column=0)
threes_display = tk.Text(window, height=1, width=15)
threes_display.grid(row=12, column=0)
twos_display = tk.Text(window, height=1, width=15)
twos_display.grid(row=13, column=0)
ones_display = tk.Text(window, height=1, width=15)
ones_display.grid(row=14, column=0)



# ---BUTTONS---
roll_button = tk.Button(window, text="Roll!", command=display_outcome).grid(row=8, column=0)
sixes_button = tk.Button(window, text="6s rolled", command=lambda: reroll(0)).grid(row=9, sticky=tk.W)
fives_button = tk.Button(window, text="5s rolled", command=lambda: reroll(1)).grid(row=10, sticky=tk.W)
fours_button = tk.Button(window, text="4s rolled", command=lambda: reroll(2)).grid(row=11, sticky=tk.W)
threes_button = tk.Button(window, text="3s rolled", command=lambda: reroll(3)).grid(row=12, sticky=tk.W)
twos_button = tk.Button(window, text="2s rolled", command=lambda: reroll(4)).grid(row=13, sticky=tk.W)
ones_button = tk.Button(window, text="1s rolled", command=lambda: reroll(5)).grid(row=14, sticky=tk.W)


window.grid_columnconfigure(4, minsize=50)
window.mainloop()
