from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)

def convert():
    miles = float(input.get())
    miles *= 1.609
    label4.config(text=f"{miles}")


label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text="km")
label3.grid(column=2, row=1)
label4 = Label(text=0)
label4.grid(column=1, row=1)

input = Entry(width=10)
input.insert(END, string=0)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

















window.mainloop()
