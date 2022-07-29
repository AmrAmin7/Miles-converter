from tkinter import *



def button_clicked():
	print("I got Clicked")
	new_input = input_entry.get()
	my_label.config(text=new_input)


window = Tk()

window.title("My First GUI Program")
window.minsize(width=500 , height=300)
window.config(padx=20 , pady=20)


# Label
my_label = Label(text="I am a Label" , font=("Arial" , 24 , "bold"))
my_label.config(text="New Text")
# my_label.place(x=100 , y=200)
my_label.grid(column=0 , row=0)
my_label.config(padx=50 , pady=50)
# my_label.pack()

# Button
button = Button(text="Click Me" , command=button_clicked)
button.grid(column=1 , row=1)
# button.pack()


# Entry
input_entry = Entry(width=10)
# input_entry.pack()
print(input_entry.get())
input_entry.grid(column=3 , row=2)



window.mainloop()
