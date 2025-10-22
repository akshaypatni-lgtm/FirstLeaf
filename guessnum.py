# guess_number.py
import random
num = random.randint(1, 100)
guess = None
while guess != num:
    guess = int(input("Guess (1–100): "))
    if guess < num: print("Too low!")
    elif guess > num: print("Too high!")
    else: print("🎉 Correct!")
