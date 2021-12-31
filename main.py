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
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
# title_label = Label(text="TIMER", font=(FONT_NAME, 25), fg=GREEN)
# title_label.place(x=50, y=5)

apple_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=apple_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# timer_label = Label(text="00:00", fg=GREEN, font=(FONT_NAME, 10))
# timer_label.place(x=180, y=170)
#
# start_button = Button(text="Start", font=(FONT_NAME, 15))
# start_button.place(x=100, y=300)
#
# stop_button = Button(text="Stop", font=(FONT_NAME, 15))
# stop_button.place(x=350, y=300)


window.mainloop()
