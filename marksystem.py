try:
    num1=int(input("enter first number:"))
    num2=int(input("enter second value:"))
    print("choose operation:+,-,*,/")
    op=input("Enter an operator:")
    if op=="+":
        print("Result:",num1+num2)
    elif op=="-":
        print("Result:",num1-num2)
    elif op=="*":
        print("Result:",num1*num2)
    elif op=="/":
        print("Result:",num1/num2)
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("Error:cannot divide by zero")
except ValueError:
    print("error:Invalid input")
else:
    print("Calculation Successful")