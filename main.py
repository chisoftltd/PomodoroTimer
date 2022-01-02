from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def cancel_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text=f"00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_count():
    global reps
    reps += 1

    work_sec = 1.5 * 60 # WORK_MIN * 60
    short_break_sec = 0.5 * 60 # SHORT_BREAK_MIN * 60
    long_break_sec = 1 * 60 # LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_count()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


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

check_label = Label(font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, command=timer_count)
start_button.grid(column=0, row=3)

stop_button = Button(text="Restart", font=(FONT_NAME, 10), highlightthickness=0, command=cancel_timer)
stop_button.grid(column=2, row=3)

window.mainloop()
