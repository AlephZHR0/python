from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global TIMER, REPS
    window.after_cancel(TIMER)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checks.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS <= 8:
        if REPS == 8:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        elif REPS % 2 == 0:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)
        elif REPS % 2 == 1:
            count_down(work_sec)
            timer_label.config(text="Work", fg=GREEN)
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text="{}:{}".format(count_min, count_sec))
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks.config(text="✔️" * (REPS // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=10, pady=10, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 55, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=8, bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", width=8, bg=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)
checks = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
checks.grid(column=1, row=3)

window.mainloop()
