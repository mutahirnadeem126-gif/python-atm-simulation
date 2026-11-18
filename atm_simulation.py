# start

initial_balance = 10000
print(f"your initial balance is {initial_balance}")

# start menu

while True:
    print("\nTake your choice:")
    print("1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        print("your current balance is", initial_balance)

    elif choice == 2:
        print("Withdrawl selected")
        withdrawl_amount = int(input("Enter your withdrawl amount:"))
        if withdrawl_amount <= initial_balance:
            if withdrawl_amount <= 0:
                print("Invalid amount")
            else:
                initial_balance = initial_balance - withdrawl_amount
                print(f"Withdraw sucessfull,Your remaining balance is {initial_balance}")
        else:
            print("Insufficient balance")

    elif choice == 3:
        print("Deposit selected")
        deposit_amount = int(input("Enter your deposit amount:"))
        if deposit_amount <= 0:
            print("invalid amount")
        else:
            initial_balance = initial_balance + deposit_amount
            print("your initial balance is ", initial_balance)

    elif choice == 4:
        print("thank you for using ATM")
        break

    else:
        print("Invalid Choice")

    