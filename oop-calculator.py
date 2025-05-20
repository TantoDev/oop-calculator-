
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
	
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
operation = input("Enter Operation,(+,-,÷,x): ")

calc = Calculator(num1, num2)

if operation == '+':
	print(f"Result: {calc.add()}")
elif operation == '-':
	print(f"Result: {calc.subtract()}")
elif operation == '÷':
	print(f"Result: {calc.divide()}")
elif operation == 'x':
	print(f"Result: {calc.multiply()}")
else:
	print("Invalid Operation!")
	
	
