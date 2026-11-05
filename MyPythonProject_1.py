import random
x = random.randint(1,100)
u = int(input("Enter your guess:"))
attempts = 0
while(u != x):
    if u < x:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    u = int(input("Enter your guess:"))
    attempts += 1
print(f"Congratulations! {x} is the right number! Got it in {attempts} attempts!")