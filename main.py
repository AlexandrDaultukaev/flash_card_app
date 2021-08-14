BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas

screen = Tk()
screen.title("Flash Card")
screen.maxsize(width=1000, height=800)
screen.minsize(width=1000, height=800)
screen.config(bg="gray", padx=10, pady=10)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
canvas = Canvas(width=1000, height=800, bg=BACKGROUND_COLOR)
canvas.create_image(500, 300, image=card_front)
canvas.create_image(600, 660, image=right)
canvas.create_image(400, 660, image=wrong)
canvas.pack()

df = pandas.read_csv("./data/english-russian.csv")
data = {row.ENG: row.RUS for (index, row) in df.iterrows()}

screen.mainloop()
