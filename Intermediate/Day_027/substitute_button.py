from tkinter import *

NUMBER_OF_CLICKED_TIMES = 0


def button_gets_clicked():
    label.config(text=entry.get())


window = Tk()
window.title("My first GUI program")
window.minsize(500, 600)

label = Label(text="New text")
label.pack()

button = Button(text="Click me", command=button_gets_clicked)
button.pack()

entry = Entry()
entry.pack()


window.mainloop()
