import random
import time

Nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
code = random.choices(Nums, k=4)
code = "".join(code)

print(code)

for i in range(0, 5):
    codeinput = input("Enter Code:")
    if len(codeinput) == 4 and codeinput.isdigit():
        if i < 4:
            if codeinput == code:
                print("Good Job")
                break
            else:
                print("Try Again")
                continue
        elif i == 4:
            print("Too many failed attempts")
            break
    else:
        print("Must be 4 digits only")
        continue

