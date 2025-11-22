from datetime import datetime

pin = "020703"
savings = 0

history = []

attempts = 3
while attempts > 0:
    input_pin = input("Enter your 6-digit PIN: ")

    if input_pin == pin:
        while True:
            print("\n--- MENU ---")
            print("1. Check Savings")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Exit")

            choice = input("Choose your option: ")

            if choice == "1":
                print("Checking Savings...")
                print(f"Your savings balance is: {savings}")

            elif choice == "2":
                deposit = float(input("Enter your deposit amount: "))
                savings += deposit

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                receipt = ("\n----- RECEIPT -----\n"
                    f"Date & Time: {timestamp}\n"
                    f"Transaction: DEPOSIT\n"
                    f"Amount: {deposit}\n"
                    f"New Balance: {savings}\n"
                )
                history.append(receipt)

                print(receipt)

            elif choice == "3":
                withdraw_amount = float(input("Enter your withdrawal amount: "))
                if withdraw_amount <= savings:
                    savings -= withdraw_amount

                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    receipt = (
                        "\n----- RECEIPT -----\n"
                        f"Date & Time: {timestamp}\n"
                        f"Transaction: WITHDRAW\n"
                        f"Amount: {withdraw_amount}\n"
                        f"Remaining Balance: {savings}\n"
                    )
                    history.append(receipt)

                    print(receipt)
                else:
                    print("Insufficient balance.")

            elif choice == "4":
                print("\n=== TRANSACTION HISTORY ===")
                if len(history) == 0:
                    print("No transaction history available.")
                else:
                    for record in history:
                        print(record)
                        print()

            elif choice == "5":
                print("Thank you for using Bank Teller")
                exit()

            else:
                print("Invalid choice. Try again")

    else:
        attempts -= 1
        print("PIN entered incorrectly")

else:
    print("Access denied")
