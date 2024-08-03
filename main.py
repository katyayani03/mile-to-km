from tkinter import *


def calculate_clicked():
    out = float(input_mile.get()) * 1.61
    km_out = str(out)
    result.config(text=km_out)


window = Tk()
window.title("Mile to Km convertor")
window.config(padx=20, pady=20)

input_mile = Entry(width=10)
input_mile.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

result = Label(text="0")
result.grid(column=1, row=1)

km_label = Message(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate_clicked)
button.grid(column=1, row=2)


window.mainloop()
