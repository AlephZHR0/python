from tkinter import *

NUMBER_OF_CLICKED_TIMES = 0


def button_gets_clicked():
    global NUMBER_OF_CLICKED_TIMES
    NUMBER_OF_CLICKED_TIMES += 1
    label["text"] = "I got clicked {} times".format(NUMBER_OF_CLICKED_TIMES)


window = Tk()
window.title("My first GUI program")
window.minsize(500, 600)

label = Label(text="New text")
label.pack()

button = Button(text="Click me", command=button_gets_clicked)
button.pack()

window.mainloop()
