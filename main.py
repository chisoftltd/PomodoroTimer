from tkinter import *
import math

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
def timer_count():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
title_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

apple_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=apple_image)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(text="✔", font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


start_button = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=timer_count)
start_button.grid(column=0, row=3)

stop_button = Button(text="Restart", font=(FONT_NAME, 10), highlightthickness=0)
stop_button.grid(column=2, row=3)

window.mainloop()
