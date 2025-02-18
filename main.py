print("GRAND DETERMINER")

date_of_birth = int(input("Please enter your birth year : "))

age= 2025- date_of_birth

print(f"You are {age} years old")

if age <=60:
    print("You don't qualify for social grand")
else:
    print("You qualify for grand")