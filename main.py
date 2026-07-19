# Expense Tracker Project

expenses_list = []  # List of expenses in dictionary form

print("Welcome to Expense Tracker: Karcha kam kiya karo 😄")

while True:
    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Please enter your choice: ")

    # 1. Add Expense
    if choice == "1":
        date = input("Kis date par karcha kiya tha? ")
        category = input(
            "Kis type ka karcha kiya? (Food, Travel, Shoes, Books): "
        )
        description = input("Expense ki details batao: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses_list.append(expense)

        print("\nDone bro! Expense successfully added.")

    # 2. View All Expenses
    elif choice == "2":
        if len(expenses_list) == 0:
            print("\nNo expenses added. Jao pehle karcha karo 😄")

        else:
            print("\n===== Ye Hai Aapka Saara Expense =====")

            count = 1

            for each_expense in expenses_list:
                print(
                    f"Karcha Number {count} -> "
                    f"Date: {each_expense['date']}, "
                    f"Category: {each_expense['category']}, "
                    f"Description: {each_expense['description']}, "
                    f"Amount: ₹{each_expense['amount']}"
                )

                count = count + 1

    # 3. View Total Expense
    elif choice == "3":
        total = 0

        for each_expense in expenses_list:
            total = total + each_expense["amount"]

        print("\nTotal Karcha = ₹", total)

    # 4. Exit
    elif choice == "4":
        print("\nThank you for using my Expense Tracker.")
        break

    else:
        print("\nInvalid choice. Please try again.")