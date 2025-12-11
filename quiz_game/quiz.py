print("Welcome to Quiz Game!")
question = input("Do you want to play?: ").lower()

if question != "yes":
    print("Maybe next time. Goodbye!")
    exit()
else:
    print("START")

score = 0

attempts = 2
while attempts > 0:
    print("Question 1")
    answer1 = input("CMOS stands for?: ").lower()
    if answer1 == "complementary metal-oxide-semiconductor":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect answer")
            print("Hint: It is a small battery that powers the memory storing BIOS/UEFI settings.")
            print(f"Attempts left: {attempts}")
        else:
            print("Incorrect! No attempts left.")
            print(f"The correct answer is: complementary metal-oxide-semiconductor")
            break
print(f"Total Score: {score}/5")

attempts = 2
while attempts > 0:
    print("\nQuestion 2")
    answer = input("What does ROM stand for? ").lower()
    if answer == "read only memory":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect answer")
            print("Hint: It is non-volatile memory used to store firmware.")
            print(f"Attempts left: {attempts}")
        else:
            print("Incorrect! No attempts left.")
            print(f"The correct answer is: read only memory")
            break
print(f"Total Score: {score}/5")

attempts = 2
while attempts > 0:
    print("\nQuestion 3")
    answer = input("What does CPU stand for? ").lower()
    if answer == "central processing unit":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect answer")
            print("Hint: It is the brain of the computer.")
            print(f"Attempts left: {attempts}")
        else:
            print("Incorrect! No attempts left.")
            print(f"The correct answer is: central processing unit")
            break
print(f"Total Score: {score}/5")

attempts = 2
while attempts > 0:
    print("\nQuestion 4")
    answer = input("What does SSD stand for? ").lower()
    if answer == "solid state drive":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect answer")
            print("Hint: It is a fast storage device with no moving parts.")
            print(f"Attempts left: {attempts}")
        else:
            print("Incorrect! No attempts left.")
            print(f"The correct answer is: solid state drive")
            break
print(f"Total Score: {score}/5")

attempts = 2
while attempts > 0:
    print("\nQuestion 5")
    answer = input("What does HDD stand for? ").lower()
    if answer == "hard disk drive":
        score += 1
        print("Congrats, you got it!")
        print(f"Score: {score}/5")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect answer")
            print("Hint: It is a traditional storage device with spinning disks.")
            print(f"Attempts left: {attempts}")
        else:
            print("Incorrect! No attempts left.")
            print(f"The correct answer is: hard disk drive")
            break
print(f"Total Score: {score}/5")

percentage = (score / 5) * 100
print("\nThank you for playing!")
print(f"Your final score: {score}/5")
print(f"Your percentage: {percentage:.2f}%")
