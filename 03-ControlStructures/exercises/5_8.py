# ATM (cash machine) simulator: check balance, deposit, withdraw, check PIN, change PIN.

balance = 1000  # Initial balance
pin = '1111'  # initial 4-digit PIN code

# my additional feature :)
# the PIN is required before the menu: 3 attempts, then the program ends 
attempts = 0
pin_ok = False
while attempts < 3 and not pin_ok:
    if input("Enter your PIN: ") == pin:
        pin_ok = True
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {3 - attempts}")

if not pin_ok:
    print("Card blocked.")
    exit()  # ends the program

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN is correct.")
        else:
            print("PIN is incorrect.")
    elif choice == '5':
        if input("Enter your current PIN: ") != pin:
            print("PIN is incorrect.")
            continue  # back to the menu, so the rest of this branch does not need else

        new_pin = input("Enter a new PIN (exactly 4 digits): ")
        # isdigit() returns True if all characters of the string are digits (and False otherwise)
        new_pin_ok = len(new_pin) == 4 and new_pin.isdigit()

        if new_pin_ok:
            pin = new_pin
            print("PIN has been changed.")
        else:
            print("Invalid PIN. It must consist of exactly 4 digits.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
