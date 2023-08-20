from tkinter import *
RESULT = 0
def calc():
    global RESULT
    label_result.config(text=round(float(entry.get()) * 1.609344, 3))


screen = Tk()
screen.config(padx=10, pady=10)

entry = Entry()
entry.grid(column=1, row=0)
entry.get()

label_is_equal_to = Label(text="Is equal to")
label_is_equal_to.grid(column=0, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)

screen.mainloop()
