from tkinter import *
import csv
import random

import pandas
# from pandas import *

import time

BACKGROUND_COLOR = "#B1DDC6"
random_foreign_word = "Merde"
foreign_word_translation = 0


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

right_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")


# Reading CSV

# data = pandas.read_csv("data/french_words.csv")
# data_dictionary = data.to_dict(orient="records")
#     def next_card():
#         current_card = random.choice(data_dictionary)
#         card_canvas.itemconfig(word_title, text=current_card["French"])

def new_word_gen():
    global random_foreign_word, foreign_word_translation, flip_timer
    window.after_cancel(flip_timer)
    data = pandas.read_csv("data/french_words.csv")
    data_dictionary = data.to_dict()
    # print(data_dictionary)
    word_number = random.randint(0, 100)
    random_foreign_word = data_dictionary["French"][word_number]
    foreign_word_translation = data_dictionary["English"][word_number]
    print(random_foreign_word)
    print(foreign_word_translation)
    card_canvas.itemconfig(word_title, text=random_foreign_word, fill="black")
    card_canvas.itemconfig(card_background, image=card_front_img)
    card_canvas.itemconfig(language_title, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)


# Flipping the card


# def count_down(count):
#     window.after(3000, count_down, count - 1)


def flip_card():
    card_canvas.itemconfig(language_title, text="English", fill="white")
    card_canvas.itemconfig(word_title, text=foreign_word_translation, fill="white")
    card_canvas.itemconfig(card_background, image=card_back_img)

# Removing the cards:

def is_known():
    data_


# Buttons

right_button = Button(image=right_button_img, highlightthickness=0, command=new_word_gen)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=new_word_gen)
wrong_button.grid(column=1, row=1)

# Canvas

card_canvas = Canvas(width=800, height=528, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = card_canvas.create_image(400, 264, image=card_front_img)
language_title = card_canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_title = card_canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
card_canvas.grid(column=0, row=0, columnspan=2)

new_word_gen()

flip_timer = window.after(3000, func=flip_card)

# print(random_foreign_word)




window.mainloop()
