o = str(input("Interpreter: ")).split()
x,y,z = o
if "+" in y:
    print(float(x) + float(z))
elif "-" in y:
    print(float(x) - float(z))
elif "/" in y:
    print(float(x) / float(z))
elif "*" in y:
    print(float(x) * float (z))