
s
class c:


    def add(self, num1, num2):

        if num1 & num2 >= 0 :
            return num1 + num2
        else:
            return num1 + num2

    def sub(self, num1, num2):

        answer = num1 - num2

        answer/2

        answer * 2

        return answer



    def multi(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2



calc = c()

#inputs numbers and operand  in calculator
num1 = float(input("input number: "))
op = input("input operand : ")
num2 = float(input("input number: "))

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