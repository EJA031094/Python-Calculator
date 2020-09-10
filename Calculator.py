import tkinter

class Calculator:

	def __init__(self, master):

		#Tracks if the entry box has a successful result. If it does, it will clear on any button click.
		self.resultSuccess = False

		#Define text field where expression will be built.
		self.entryBox = tkinter.Entry(master, width = 50, borderwidth = 5, state = "disabled")

		#Define numeral buttons.
		self.button_0 = tkinter.Button(master, text = "0", padx = 30, pady = 20, command = lambda:self.button_numeral_click(0))
		self.button_1 = tkinter.Button(master, text = "1", padx = 30, pady = 20, command = lambda:self.button_numeral_click(1))
		self.button_2 = tkinter.Button(master, text = "2", padx = 30, pady = 20, command = lambda:self.button_numeral_click(2))
		self.button_3 = tkinter.Button(master, text = "3", padx = 30, pady = 20, command = lambda:self.button_numeral_click(3))
		self.button_4 = tkinter.Button(master, text = "4", padx = 30, pady = 20, command = lambda:self.button_numeral_click(4))
		self.button_5 = tkinter.Button(master, text = "5", padx = 30, pady = 20, command = lambda:self.button_numeral_click(5))
		self.button_6 = tkinter.Button(master, text = "6", padx = 30, pady = 20, command = lambda:self.button_numeral_click(6))
		self.button_7 = tkinter.Button(master, text = "7", padx = 30, pady = 20, command = lambda:self.button_numeral_click(7))
		self.button_8 = tkinter.Button(master, text = "8", padx = 30, pady = 20, command = lambda:self.button_numeral_click(8))
		self.button_9 = tkinter.Button(master, text = "9", padx = 30, pady = 20, command = lambda:self.button_numeral_click(9))

		#Define operation buttons.
		self.button_add = tkinter.Button(master, text = "+", padx = 29, pady = 20, command = self.button_addition)
		self.button_subtract = tkinter.Button(master, text = "-", padx = 30, pady = 20, command = self.button_subtraction)
		self.button_multiply = tkinter.Button(master, text = "*", padx = 30, pady = 20, command = self.button_multiplication)
		self.button_divide = tkinter.Button(master, text = "/", padx = 30, pady = 20, command = self.button_division)
		self.button_equal = tkinter.Button(master, text = " = ", padx = 65, pady = 20, command = self.button_equal_op)
		self.button_clear = tkinter.Button(master, text = "Clear", padx = 60, pady = 20, command = self.button_clear_op)

		#Layout text field.
		self.entryBox.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

		#Layout numeral buttons.
		self.button_0.grid(row = 4, column = 0)
		self.button_1.grid(row = 3, column = 0)
		self.button_2.grid(row = 3, column = 1)
		self.button_3.grid(row = 3, column = 2)
		self.button_4.grid(row = 2, column = 0)
		self.button_5.grid(row = 2, column = 1)
		self.button_6.grid(row = 2, column = 2)
		self.button_7.grid(row = 1, column = 0)
		self.button_8.grid(row = 1, column = 1)
		self.button_9.grid(row = 1, column = 2)

		#Layout operation buttons.
		self.button_add.grid(row = 1, column = 3)
		self.button_subtract.grid(row = 2, column = 3)
		self.button_multiply.grid(row = 3, column = 3)
		self.button_divide.grid(row = 4, column = 3)
		self.button_equal.grid(row = 5, column = 2, columnspan = 2)
		self.button_clear.grid(row = 5, column = 0, columnspan = 2)

		#Define lists to contain operators/operands.
		self.operandList = []
		self.operatorList = []

	#One of the 10 numeral buttons was clicked, update current expression accordingly.
	def button_numeral_click(self, number):

		self.clearResult()

		self.entryBox.configure(state = "normal")
		current = self.entryBox.get()
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, str(current) + str(number))
		self.entryBox.configure(state = "disabled")

	#Concatenates an addition operator onto the current expression.
	def button_addition(self):

		self.clearResult()

		self.entryBox.configure(state = "normal")
		current = self.entryBox.get()
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, str(current) + " + ")
		self.entryBox.configure(state = "disabled")

	#Concatenates a subtraction operator onto the current expression.
	def button_subtraction(self):

		self.clearResult()

		self.entryBox.configure(state = "normal")
		current = self.entryBox.get()
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, str(current) + " - ")
		self.entryBox.configure(state = "disabled")

	#Concatenates a multiplication operator onto the current expression.
	def button_multiplication(self):

		self.clearResult()

		self.entryBox.configure(state = "normal")
		current = self.entryBox.get()
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, str(current) + " * ")
		self.entryBox.configure(state = "disabled")

	#Concatenates a division operator onto the current expression.
	def button_division(self):

		self.clearResult()

		self.entryBox.configure(state = "normal")
		current = self.entryBox.get()
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, str(current) + " / ")
		self.entryBox.configure(state = "disabled")

	#Attempts to parse the current expression from the entry box and then evaluate a result from the operand and operator lists.
	#If the expression can not be evaluated, catches the resulting error and displays a message in entryBox.
	def button_equal_op(self):

		self.clearResult()

		try:

			self.parse_expression()
			self.evaluate_expression()

			self.operandList = []
			self.operatorList = []

		except:

			self.entryBox.configure(state = "normal")
			self.entryBox.delete(0, tkinter.END)
			self.entryBox.insert(0, "Error, an invalid expression was entered.")
			self.entryBox.configure(state = "disabled")

			#Error message counts as result, causes the error to clear on next button press.
			self.resultSuccess = True

			self.operandList = []
			self.operatorList = []

	def button_clear_op(self):
		self.entryBox.configure(state = "normal")
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.configure(state = "disabled")

	#Breaks the final expression into operands and operators, storing them in operandList and operatorList respectively.
	def parse_expression(self):
		expression = self.entryBox.get()
		currentOperand = ""

		for character in expression:

			#The parser found a numeral, add it to currentOperand string.
			if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:

				currentOperand = currentOperand + character

			#The parser found an operator.
			elif character in ["+", "-", "*", "/"]:
				self.operatorList.append(character)

			#If the character is neither an operator or a numeral it must be a space, signifying the termination of the current operand or operator.
			#Because there is a space after every operator, check that currentOperand is not "".
			else:
				if(currentOperand != ""):
					self.operandList.append(float(currentOperand))
					currentOperand = ""

		#The above loop uses spaces to determine where an operand terminates. Because there is no space at the end of the expression
		#we need to append the final operand to the list.
		if(currentOperand != ""):

			self.operandList.append(float(currentOperand))

	#Calculates the result of the expression and puts it in entryBox. If this throws an error it will be caught in button_equal_op, signifying a malformed expression.
	def evaluate_expression(self):

		index = 0

		#Evaluates any multiplications or division operators.
		while(("*" in self.operatorList) or ("/" in self.operatorList)):

			if(len(self.operatorList) == 0):
				break

			if self.operatorList[index] == "*":

				result = self.operandList[index] * self.operandList[index + 1]
				self.operandList[index] = result
				del self.operandList[index + 1]
				del self.operatorList[index]
				index = 0
				continue

			elif self.operatorList[index] == "/":

				result = self.operandList[index] / self.operandList[index + 1]
				self.operandList[index] = result
				del self.operandList[index + 1]
				del self.operatorList[index]
				index = 0
				continue

			index += 1

		index = 0

		#Evaluates any addition or subtraction operators.
		while(("+" in self.operatorList) or ("-" in self.operatorList)):

			if(len(self.operatorList) == 0):
				break

			if self.operatorList[index] == "+":

				result = self.operandList[index] + self.operandList[index + 1]
				self.operandList[index] = result
				del self.operandList[index + 1]
				del self.operatorList[index]
				index = 0
				continue

			elif self.operatorList[index] == "-":

				result = self.operandList[index] - self.operandList[index + 1]
				self.operandList[index] = result
				del self.operandList[index + 1]
				del self.operatorList[index]
				index = 0
				continue

			index += 1

		self.entryBox.configure(state = "normal")
		self.entryBox.delete(0, tkinter.END)
		self.entryBox.insert(0, self.operandList[0])
		self.entryBox.configure(state = "disabled")
		self.resultSuccess = True

	#Checks if the entryBox contains a result and clears it if so.
	def clearResult(self):

		if self.resultSuccess:

			self.entryBox.configure(state = "normal")
			self.entryBox.delete(0, tkinter.END)
			self.entryBox.configure(state = "disabled")
			self.resultSuccess = False