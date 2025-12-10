print("Welcome to Quiz Game!")
question = input("Do you want to play?: ")

while True:
    if question.lower() == "no":
        break
    else:
        print("START")

        score = 0

        attempts = 2
        while attempts > 0:
            print("Question 1")
            answer1 = input("CMOS stands for?: ")
            if answer1.lower() == "complementary metal-oxide-semiconductor":
                score += 1
                print("Correct!")
                print(f"Score: {score}/5")
                break

            else:
                print("Incorrect answer")
                print("Hint: It is a small battery that powers the memory storing BIOS/UEFI settings.")
                attempts -= 1
                print(f"Total Score: {score}/5")

        if attempts == 0:
                break

        print("\nQuestion 2")
        answer = input("What does ROM stand for? ")
        if answer.lower() == "read only memory":
            score += 1
            print("Correct!")
            print(f"Score: {score}/5")
        else:
            print("Incorrect! \nThanks for playing!")
            print(f"Score: {score}/5")
            break


    print("\nQuestion 3")
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
    else:
        print("Incorrect! \nThanks for playing!")
        print(f"Score: {score}/5")
        break

    print("\nQuestion 4")
    answer = input("What does SSD stand for? ")
    if answer.lower() == "solid state drive":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
    else:
        print("Incorrect! \nThanks for playing!")
        print(f"Score: {score}/5")
        break

    print("\nQuestion 5")
    answer = input("What does HDD stand for? ")
    if answer.lower() == "hard disk drive":
        score += 1
        print("Congrats, you got it!")
        print(f"Score: {score}/5")
        break
    else:
        print("Incorrect! \nThanks for playing!")
        print(f"Score: {score}/5")
        print(f"You got {(score + (score / 5) * 100)}%")
        break
