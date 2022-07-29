from tkinter import *


def calculate():
	miles = float(input_entry.get())
	km = miles * 1.60934
	result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50 , height=50)
window.config(padx=30 , pady=30)

equal_label = Label(text="is equal to")
equal_label.grid(column=0 , row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2 , row=0)
km_label = Label(text="Km")
km_label.grid(column=2 , row=1)

result_label = Label(text="0")
result_label.grid(column=1 , row=1)

button = Button(text="Calculate" , command=calculate)
button.grid(column=1 , row=2)

input_entry = Entry(width=10)
input_entry.grid(column=1 , row=0)

window.mainloop()
