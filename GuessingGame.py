import random

def guess(x):
    random_num = random.randint(1, x)

    guess = int(input("guess the number"))

    while guess != random_num:

        if guess < random_num:
            guess = int(input("u guessed too low, guess again!"))
        elif guess > random_num:
            guess = int(input("you guessed toohigh, guess again"))
    print(f"congrats! you guessed the number {guess} right")
x = int(input("upto what do you want your guessing range should be"))

guess(x)