import random
x = random.randint(1,100)
u = int(input("Enter your guess:"))
while(u != x):
    if u < x:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    u = int(input("Enter your guess:"))
print(f"Congratulation! {x} is the right number!")