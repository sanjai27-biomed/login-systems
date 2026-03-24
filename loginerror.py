try:
    username=input("enter username:")
    password=input("enter password:")

    if username=="admin"and password=="1234":
        print("Login Successful")
    elif username==" "or password==" ":
        raise ValueError("Empty input not allowed")
    else:
        print("Invalid credentials")
except ValueError as e:
    print("error",e)
finally:
    print("Login execution completed")