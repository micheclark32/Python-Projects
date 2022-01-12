import random
import string
from tkinter import *
from tkinter.ttk import *


# function for random password

def password_props():
    entry.delete(0, END)

    # Get the length of password
    length = length_choice.get()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    combine = lower + upper + digits

    # for loop for when length is selected

    for i in range(0, length):
        password = random.sample(combine, length)
    return password


# Function for generate button
def generate():
    final_password = password_props()
    entry.insert(10, final_password)


def main():
    root = Tk()
    length_choice = IntVar()
    frame = Frame(root)

    # Title of your GUI window
    root.title("Random Password Generator")

    # call main_window to build labels

    # start the GUI
root.mainloop()


def main_window():
    # create label and entry to show
    # password generated
    p_label = Label(root, text="Password")
    p_label.grid(row=1)
    entry = Entry(root)
    entry.grid(row=1, column=1)

    # create label for length of password
    c_label = Label(root, text="Select number of Characters:")
    c_label.grid(row=0)

    # Generate button which will generate the password

    generate_button = Button(root, text="Generate", command=generate)
    generate_button.grid(row=1, column=3)

    list = Combobox(root, textvariable=length_choice)

    # Combo Box for length of your password
    list['values'] = (8, 9, 10, 11, 12, 13, 14, 15)
    list.current(0)
    list.bind('<<ComboboxSelected>>')
    list.grid(column=1, row=0)
