from tkinter import *

def button_addition():
	entryBox.configure(state="normal")
	first_operand=entryBox.get()
	f_operand=int(first_operand)
	entryBox.delete(0, END)
	entryBox.configure(state="disabled")

def button_click(number):
	entryBox.configure(state="normal")
	current=entryBox.get()
	entryBox.delete(0, END)
	entryBox.insert(0, str(current)+str(number))
	entryBox.configure(state="disabled")

def button_clear():
	entryBox.configure(state="normal")
	entryBox.delete(0, END)
	entryBox.configure(state="disabled")

def button_equal():
	entryBox.configure(state="normal")
	second_number=entryBox.get()
	entryBox.delete(0, END)
	entryBox.insert(0, f_operand + int(second_number))
	entryBox.configure(state="disabled")

#Root widget
root=Tk()
root.title("Calculator")

#Define text field

entryBox=Entry(root, width=50, borderwidth=5, state="disabled")
entryBox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Define numeral buttons
button_0=Button(root, text="0", padx=30, pady=20, 
	command=lambda: button_click(0)).grid(row=4, column=0)
button_1=Button(root, text="1", padx=30, pady=20, 
	command=lambda:button_click(1)).grid(row=3, column=0)
button_2=Button(root, text="2", padx=30, pady=20, 
	command=lambda:button_click(2)).grid(row=3, column=1)
button_3=Button(root, text="3", padx=30, pady=20, 
	command=lambda:button_click(3)).grid(row=3, column=2)
button_4=Button(root, text="4", padx=30, pady=20, 
	command=lambda:button_click(4)).grid(row=2, column=0)
button_5=Button(root, text="5", padx=30, pady=20, 
	command=lambda:button_click(5)).grid(row=2, column=1)
button_6=Button(root, text="6", padx=30, pady=20, 
	command=lambda:button_click(6)).grid(row=2, column=2)
button_7=Button(root, text="7", padx=30, pady=20, 
	command=lambda:button_click(7)).grid(row=1, column=0)
button_8=Button(root, text="8", padx=30, pady=20, 
	command=lambda:button_click(8)).grid(row=1, column=1)
button_9=Button(root, text="9", padx=30, pady=20, 
	command=lambda:button_click(9)).grid(row=1, column=2)

#Define operation buttons
button_add=Button(root, text="+", padx=29, pady=20, 
	command=button_addition).grid(row=1, column=3)
button_subtract=Button(root, text="-", padx=31, pady=20, 
	command=button_addition).grid(row=2, column=3)
button_multiply=Button(root, text="*", padx=31, pady=20, 
	command=button_addition).grid(row=3, column=3)
button_divide=Button(root, text="/", padx=31, pady=20, 
	command=button_addition).grid(row=4, column=3)
button_equal=Button(root, text="=", padx=70, pady=20, 
	command=button_equal).grid(row=5, column=2, columnspan=2)
button_clear=Button(root, text="Clear", padx=62, pady=20, 
	command=button_clear).grid(row=5, column=0, columnspan=2)


root.mainloop()