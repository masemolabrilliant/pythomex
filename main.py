age = int(input("How old are you? "))
gender = input("WHat is your gender, (M/F)")

if gender == "F" and age >= 15 :
    print("You are welcome girl")
elif gender == "M" and age >= 17:
    print("You are welcome boy")
else:
    print("For males you must be 17 older for femlane you must be 15 and above")
