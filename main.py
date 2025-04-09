#calculator

num1,sign, num2= input("Enter fisrt number, sign and second number: ").split()
num1= float(num1)
num2 = float(num2)

if sign=="+":
    print(f"The sum is : {num1 + num2}")
elif sign=="-":
    print(f"Answer is : {num1 - num2}")
elif sign=="*":
    print(f"Answer is  : {num1 * num2}")
elif sign=="/":
    print(f"Answer is  : {num1 / num2}")
elif sign=="%":
    print(f"Answer is  : {num1 % num2}")
else:
    print(f"invalid operator {sign}")

