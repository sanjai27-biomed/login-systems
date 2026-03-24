try:
    email=input("enter mail:")
    if "@" not in email or "." not in email:
        raise Exception("Invalid email format")
    print("valid email format")
except Exception as e:
    print("Error:",e)
