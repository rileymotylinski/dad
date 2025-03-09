import time
import sys

with open("birthday_card.txt", "r") as f:
    for line in f:
        for c in line:
            time.sleep(0.05)
            sys.stdout.write(c)
            sys.stdout.flush()

        time.sleep(0.5)