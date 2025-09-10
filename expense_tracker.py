def main():
    # load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Exit")
        choice = input("Choose (1-3): ")   

        if choice == "1":
            try:
                description = input("Description: ").strip()
                amount_str = input("Amount(e.g., 10.50): ")
                category = input("Category(food, transport, fun): ").lower()

                # amount = check_amount( amount_str)
                if amount is None:
                    print("invalid amount. use format like 10 or 10.50")
                    continue 

                # add_expense(description, amount, category)
            except ValueError as e:
                print(f"Error:{e}")

            except Exception as e:
                print(f"Exception error:{e}")


        elif choice == "2":
            # show_expense()
            print("show expense")

        elif choice == "3":
            print("goobye")
            break 
        
        else:
            print("choose 1,2 or 3")


if __name__ == "__main__":
    main()