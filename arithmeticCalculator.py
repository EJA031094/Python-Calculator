import tkinter
import Calculator

#Root widget
root = tkinter.Tk()
root.title("Arithmetic Calculator")

myCalculator = Calculator.Calculator(root)

root.mainloop()