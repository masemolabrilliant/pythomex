import math

adj = int(input("Enter adjacent? "))

opp = int(input("Enter opposite? "))

hyp =  math.sqrt(pow(adj,2) + pow(opp,2))

print(f"The hypothenus is {hyp}")