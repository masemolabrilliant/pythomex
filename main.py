##ask a user for a name
import time

timecounter = int(input("what is you name: "))

for x in reversed(range(0, timecounter)):
    print(f"00:00:{x:02}")
    time.sleep(1)