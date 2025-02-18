#shoping ticket

item = input("What do you need? ")
price = float(input(f"How much is one {item} R "))
quantity = int(input(f"how many {item} do you need? "))

print(f"You bought******"
      f"{item} R{price} *{quantity} Total R{price*quantity}")