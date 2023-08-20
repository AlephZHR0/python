from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="record")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(CURRENT_CARD)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global CURRENT_CARD, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)
    CURRENT_CARD = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=CURRENT_CARD["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card_image)
    FLIP_TIMER = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_background, image=back_card_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_title, text=CURRENT_CARD["English"], fill="white")

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# Images
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

FLIP_TIMER = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(800 / 2, 526 / 2, image=front_card_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
# Buttons
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()