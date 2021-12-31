# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.minsize(width=600, height=400)


title_label = Label(text="TIMER", font=(FONT_NAME, 25), fg=GREEN)
title_label.place(x=250, y=15)


apple_image = Image.open("tomato.png")
apple_image_tk = ImageTk.PhotoImage(apple_image)

apple_label = Label(image=apple_image_tk)
apple_label.image = apple_image_tk
apple_label.place(x=200, y=50)

timer_label = Label(text="00:00", fg=GREEN, font=(FONT_NAME, 10))
timer_label.place(x=280, y=170)

start_button = Button(text="Start", font=(FONT_NAME, 15))
start_button.place(x=100, y=300)

stop_button = Button(text="Stop", font=(FONT_NAME, 15))
stop_button.place(x=450, y=300)


window.mainloop()
