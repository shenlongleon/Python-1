# first_module.py

def add(a, b):
    c = a + b
    return c, "+"

def subtract(a, b):
    c = a - b
    return c, "-"

def multiply(a, b):
    c = a * b
    return c, "*"

def divide(a, b):
    c = a / b

    return c, "/"

a = float(47)
b = float(7)

answer, symbol = add(a, b)
print("{} {} {} = {}".format(a, symbol, b, int(answer)))
answer, symbol = subtract(a, b)
print("{} {} {} = {}".format(a, symbol, b, int(answer)))
answer, symbol = multiply(a, b)
print("{} {} {} = {}".format(a, symbol, b, int(answer)))
answer, symbol = divide(a, b)
print("{} {} {} = {}".format(a, symbol, b, answer))

print("======================")
print("Additional practice")
x = input("Enter the first number: ")
y = input("Enter the second number: ")
symb = raw_input("Enter the operation(+,-,*,/): ")
xx = float(x)
yy = float(y)
if symb == "+":
    answer_, symbol_ = add(xx,yy)
elif symb == "-":
    answer_, symbol_ = subtract(xx,yy)
elif symb == "*":
    answer_, symbol_ = multiply(xx,yy)
elif symb == "/":
    answer_, symbol_ = divide(xx,yy)
else:
    print("Error: please input properly")
print("{} {} {} = {}".format(xx, symbol_, yy, answer_))
