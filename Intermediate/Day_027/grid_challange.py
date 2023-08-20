from tkinter import *
screen = Tk()

label = Label(text="Label")
label.grid(column=0, row=0)
button = Button(text="Click me")
button.grid(column=1, row=1)
new_button = Button(text="Another button")
new_button.grid(column=2, row=0)
entry = Entry()
entry.grid(column=3, row=2)

screen.mainloop()
