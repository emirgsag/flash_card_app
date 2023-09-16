from tkinter import *
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


# WORD CHOICE
def word_choice():
    global wait, current_word
    window.after_cancel(wait)
    current_word = choice(word_dict)

    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(word, text=current_word["French"])
    canvas.itemconfig(title, text="French")
    wait = window.after(3000, flip_card)


def known_word():
    global word_dict, current_word
    word_dict.remove(current_word)
    word_choice()


def flip_card():
    global current_word
    canvas.itemconfig(image, image=card_back)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_word["English"])


# USER INTERFACE
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=known_word)
right_button.grid(row=1, column=1)

worng_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=worng_image, highlightthickness=0, borderwidth=0, command=word_choice)
wrong_button.grid(row=1, column=0)

wait = window.after(3000, flip_card)
word_choice()

window.mainloop()
pandas.DataFrame(data=word_dict).to_csv(path_or_buf="data/words_to_learn.csv", index=False)
