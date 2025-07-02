
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

#Dictionary for operation select
operations = {
    "+": calc.add,
    "-": calc.sub,
    "*": calc.multi,
    "/": calc.div
}

#selects operations
operation_select = operations.get(op)


#Prints out result
if operation_select:
    print(operation_select(num1, num2))
else:
    print("Invalid operator")

