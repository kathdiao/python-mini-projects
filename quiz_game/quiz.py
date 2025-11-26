print("Welcome to Quiz Game!")
question = input("Do you want to play?")
score = 0

while True:
    if question.lower() != "yes":
        break
    else:
        print("Let's play")

        answer = input("What does RAM stand for? ")
        if answer.lower() == "random access memory":
            score += 1
            print("Correct!")
            print(f"Score: {score}/5")

        else:
            print("Incorrect! \nThanks for playing!")
            print(f"Score: {score}/5")
            break

        answer = input("What does ROM stand for? ")
        if answer.lower() == "read only memory":
            score += 1
            print("Correct!")
            print(f"Score: {score}/5")
        else:
            print("Incorrect! \nThanks for playing!")
            print(f"Score: {score}/5")
            break

    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
    else:
        print("Incorrect! \nThanks for playing!")
        print(f"Score: {score}/5")
        break

    answer = input("What does SSD stand for? ")
    if answer.lower() == "solid state drive":
        score += 1
        print("Correct!")
        print(f"Score: {score}/5")
    else:
        print("Incorrect! \nThanks for playing!")
        print(f"Score: {score}/5")
        break

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
