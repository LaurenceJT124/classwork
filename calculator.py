
# calculator class and functions
class calc:

    #Addition function
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2

##Starts calculator
calc = calc()

#inputs numbers and operand  in calculator
num1 = float(input("first number: "))
op = input("input operand +, -, *, / : ")
num2 = float(input("second number: "))

#prints output depending on operand
if op == "+":
    print(calc.add(num1, num2))
elif op == "-":
    print(calc.sub(num1, num2))
elif op == "*":
    print(calc.multi(num1, num2))
elif op == "/":
    print(calc.div(num1, num2))
else:
    print("Invalid operator")