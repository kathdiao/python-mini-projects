print("Welcome to Quiz Game!")
play = input("Do you want to play? (yes/no): ").lower()

if play != "yes":
    print("Maybe next time. Goodbye!")
    exit()

print("\nLet's start the quiz!\n")
score = 0

quiz = [
    {
        "question": "CMOS stands for?: ",
        "answer": "complementary metal-oxide-semiconductor",
        "hint": "It is a small battery that powers the memory storing BIOS/UEFI settings."
    },
    {
        "question": "What does ROM stand for?: ",
        "answer": "read only memory",
        "hint": "It is non-volatile memory used to store firmware."
    },
    {
        "question": "What does CPU stand for?: ",
        "answer": "central processing unit",
        "hint": "It is the brain of the computer."
    },
    {
        "question": "What does SSD stand for?: ",
        "answer": "solid state drive",
        "hint": "It is a fast storage device with no moving parts."
    },
    {
        "question": "What does HDD stand for?: ",
        "answer": "hard disk drive",
        "hint": "It is a traditional storage device with spinning disks."
    }
]

for idx, q in enumerate(quiz, start=1):
    attempts = 2
    while attempts > 0:
        print(f"\nQuestion {idx}")
        answer = input(q["question"]).lower()
        if answer == q["answer"]:
            score += 1
            print("Correct!")
            print(f"Score: {score}/{len(quiz)}")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect!")
                print(f"Hint: {q['hint']}")
                print(f"Attempts left: {attempts}")
            else:
                print("Incorrect! No attempts left.")
                print(f"The correct answer is: {q['answer']}")
                break

percentage = (score / len(quiz)) * 100
print("\nQuiz finished!")
print(f"Your final score: {score}/{len(quiz)}")
print(f"Your percentage: {percentage:.2f}%")
print("Thank you for playing!")
