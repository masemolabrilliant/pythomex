#Calculator

num1 = float(input("Enter your first value: "))
num2 = float(input("Enter your second value: "))
operator = input("Enter the operator *,/,-,+ :")

if operator == "+":
    print(f"Results of {num1} + {num2} = {num1+num2}")
elif operator == "-":
    print(f"Results of {num1} - {num2} = {num1-num2}")
elif operator == "*":
    print(f"Results of {num1} * {num2} = {num1*num2}")
elif operator == "/":
    print(f"Results of {num1} / {num2} = {num1/num2}")
