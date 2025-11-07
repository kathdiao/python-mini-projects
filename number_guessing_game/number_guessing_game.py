import random

top_of_range = input("Type a number: ")

#will not include the last number (10)
#r = random.randrange(1, 10)
#print(r)

#it will include the last number (10)
#r = random.randint(1, 10)
#print(r)

if top_of_range.isdigit():
    #convert string into integer
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please enter a number: ")
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number: ")
    if guess.isdigit():
        # convert string into integer
        guess = int(guess)

    else:
        print("Please enter valid number ")
        continue

    if guess == random_number:
        print("Your guessed right!")
        break
    else:
        if guess < random_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

print(f"You got it in {guesses} guesses")