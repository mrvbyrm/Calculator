print("*****************************")

print("Calculator Program\n")
print("1-Addition Operation")
print("2-Subtraction Operation")
print("3-Multiplication Operation")
print("4-Division Operation")
print("*****************************")
op=input("Enter Operation:")
if(op=="1"):
    print("op:+")
    n1 = float(input("First number:"))
    n2 = float(input("Second number:"))
    print("Result=",(n1+n2))
elif(op=="2"):
    print("op:-")
    n1 = float(input("First number:"))
    n2 = float(input("Second number:"))
    print("Result=", (n1 - n2))
elif(op=="3"):
    print("op:x")
    n1 = float(input("First number:"))
    n2 = float(input("Second number:"))
    print("Result=", (n1 * n2))
elif(op=="4"):
    print("op:/")
    n1 = float(input("First number:"))
    n2 = float(input("Second number:"))
    if(n2!=0):
        print("Result=", (n1 / n2))
    else:
        print("Invalid Operation!Division by zero is not allowed.")
else:
    print("Error!Invalid Operation...")
