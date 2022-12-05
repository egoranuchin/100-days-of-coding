from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Label

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

number_km = Label(text="0")
number_km.grid(column=1, row=1)

Miles = Label(text="Miles")
Miles.grid(column=2, row=0)

Km = Label(text="Km")
Km.grid(column=2, row=1)

# Button

def calculate():
    result = round(int(input.get())*1.609344,2)
    number_km["text"] = f"{result}"

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# Entry

input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())

window.mainloop()