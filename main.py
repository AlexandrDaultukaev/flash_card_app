from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def flip_card():
    label_top.config(text="RUS", bg="#92c3b0", fg="white")
    label.config(text=current_word["RUS"], bg="#92c3b0", fg="white",
                 anchor=CENTER)
    canvas.itemconfig(card_img, image=card_back)


def next_card(is_right):
    global current_word
    if is_right:
        del to_learn[to_learn.index(current_word)]
    canvas.itemconfig(card_img, image=card_front)
    current_word = random.choice(to_learn)
    label_top.config(text="ENG", bg="white")
    label.config(text=current_word["ENG"],
                 anchor=CENTER, bg="white")
    canvas.after(5000, flip_card)


screen = Tk()
screen.title("Flash Card")
screen.maxsize(width=1000, height=800)
screen.minsize(width=1000, height=800)
screen.config(bg=BACKGROUND_COLOR, padx=10, pady=10)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_png = PhotoImage(file="./images/right.png")
wrong_png = PhotoImage(file="./images/wrong.png")
canvas = Canvas(width=1000, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(500, 300, image=card_front)
canvas.pack()

right = Button(image=right_png, borderwidth=0, highlightthickness=0, command=lambda: next_card(1))
right.place(x=550, y=610)

wrong = Button(image=wrong_png, borderwidth=0, highlightthickness=0, command=lambda: next_card(0))
wrong.place(x=350, y=610)

df = pandas.read_csv("./data/english-russian.csv")
to_learn = df.to_dict(orient="records")

label_top = Label(text="ENG", font=("Ariel", 28, "italic"), bg="white")
label_top.place(x=445, y=100)
current_word = random.choice(to_learn)
label = Label(text=current_word["ENG"], font=("Ariel", 38, "bold"),
              anchor=CENTER, bg="white")
label.place(x=415, y=300)
screen.after(5000, flip_card)
screen.mainloop()
