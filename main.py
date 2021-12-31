from tkinter import *
from PIL import Image, ImageTk
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


window = Tk()
window.minsize(width=600, height=400)
window.title("POMODORO")

canvas = Canvas(width=200, height=224)
title_label = Label(text="TIMER", font=(FONT_NAME, 25), fg=GREEN)
title_label.place(x=250, y=15)

apple_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=apple_image)
canvas.pack()

timer_label = Label(text="00:00", fg=GREEN, font=(FONT_NAME, 10))
timer_label.place(x=280, y=170)

start_button = Button(text="Start", font=(FONT_NAME, 15))
start_button.place(x=100, y=300)

stop_button = Button(text="Stop", font=(FONT_NAME, 15))
stop_button.place(x=450, y=300)


window.mainloop()
