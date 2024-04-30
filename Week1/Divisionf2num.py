a=input("Enter a:")
b=input("Enter b:")

acopy=a.replace(".", "")
bcopy=b.replace(".", "")

if((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric())):
    print(float(a)/float(b))
else:
    print("Enter a numerical value")