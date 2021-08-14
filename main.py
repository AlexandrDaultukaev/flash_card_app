from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"


def run():
    canvas.delete("front")
    canvas.create_image(500, 300, image=card_back, tag="back")


def reset():
    canvas.delete("back")
    canvas.create_image(500, 300, image=card_front, tag="front")
    canvas.after(5000, run)


screen = Tk()
screen.title("Flash Card")
screen.maxsize(width=1000, height=800)
screen.minsize(width=1000, height=800)
screen.config(bg="gray", padx=10, pady=10)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_png = PhotoImage(file="./images/right.png")
wrong_png = PhotoImage(file="./images/wrong.png")
canvas = Canvas(width=1000, height=800, bg=BACKGROUND_COLOR)
canvas.create_image(500, 300, image=card_front, tag="front")
canvas.pack()

right = Button(image=right_png, borderwidth=0, highlightthickness=0, command=reset)
right.place(x=550, y=610)

wrong = Button(image=wrong_png, borderwidth=0, highlightthickness=0)
wrong.place(x=350, y=610)

screen.after(5000, run)

df = pandas.read_csv("./data/english-russian.csv")
data = {row.ENG: row.RUS for (index, row) in df.iterrows()}

screen.mainloop()
