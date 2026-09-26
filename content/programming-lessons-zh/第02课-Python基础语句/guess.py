from random import randint

secret = randint(1, 20)
print("I am thinking of a number between 1 and 20!")

tries = 0
while True:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess == secret:
        print("You got it!")
        print("Tries:", tries)
        break
    elif guess < secret:
        print("Too small, go bigger!")
    else:
        print("Too big, go smaller!")
