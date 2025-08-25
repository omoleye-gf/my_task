# # Task1
# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.



USSD_code =input("Enter your USSD code:")
print(f"your USSD CODE is: {USSD_code}")
    
#else:
print("Welcome back you can do all your transaction here ")
while True:
        print("\naccount Menu:")
        print("1. Check Balance")
        print("2. Buy data")
        print("3. Buy airtime")
        choice = input("Enter your choice here")
        if choice == "1":
            print(f" your USSD CODE is: {USSD_code}")

        elif choice == "2":
            amount = int(input("Enter the amount you want to withdraw:"))
            if amount <= USSD_code:
                USSD_code -= amount
                print(f"withdraw sucessfully.   New code: {USSD_code}")
            else:
                print("Invalid code")
        elif choice == "3":
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid codes. pls try again next time.")

# Comment
print("Hello World")