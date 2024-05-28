import random

default_random = random.randint(1, 100)

def guess(x):
  random_number = random.randint(1, x)
  guess = 0

  while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {x}\n"))

    if guess < random_number:
      print("Try again, your number was too low.")
    elif guess > random_number:
      print("Try again, your number was too high.")

  print(f"Congratulations, you guessed the number {random_number} correctly!")


guess(default_random)
