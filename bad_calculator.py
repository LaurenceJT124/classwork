



class c:


    def add(self, num1, num2):

        if num1 & num2 >= 0 :
            return num1 + num2
        else:
            return num1 + num2

    def sub(self, num1, num2):

        answer = num1 - num2

        answer = answer/2

        answer = answer * 2

        return answer



    def multi(self, num1, num2):

        index = 42

        if index > 0 :
            return num1 * num2

        return 0

    def div(self, num1, num2):


        return num1 / num2



c = c()




n1 = float(input("input number: "))
o = input("input operand : ")
n2 = float(input("input number: "))


if o == "+":
    print(c.add(n1, n2))





















elif o == "-":
    print(c.sub(n1, n2))























elif o == "*":












    print(c.multi(n1, n2))
elif o == "/":
    print(c.div(n1, n2))








else:
    print("invalid operator")