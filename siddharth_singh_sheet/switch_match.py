print("welcome to basic calculator")

num1= int(input("enter the first number : "))

num2= int(input("enter the second number : "))

operand=input("enter the opeartor ( + , - , * , / ) : ")

match operand:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)