import random

num = int(input("enter the number what is was thinking : "))

guess = random.randin(1,10)

for num in guess:
    if num > guess:
        print("guess is higher.")
        else:
            if num<guess:
                print("guess is lower.")
            else:
                if num == guess:
                    print("you won")
                    break
