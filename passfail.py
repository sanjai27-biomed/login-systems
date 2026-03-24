try:
    mark=int(input("enter mark:"))
    if mark<0 or mark>100:
        raise Exception("invalid mark range")
    if mark>=90:
        print("Grade:S")
    elif mark>=80:
        print("Grade:A")
    elif mark>=60:
        print("Grade:B")
    elif mark>=50:
        print("Grade:C")
    else:
        print("Fail")
except ValueError:
    print("invalid input")
    