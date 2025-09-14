import os
import re

DATA_FILE = "expenses.txt"
CATEGORIS = ("food", "transport", "fun")
expenses = []

def load_expenses():
    global expenses

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE,"r") as file:
                for line in file:
                    parts = line.strip().split(",")    #if it gets "," it will split the line
                    print("# ,#, #", parts)
                    if len(parts) == 3:
                        expenses.append({
                            "description": parts[0],
                            "amount": parts[1],  
                            "category":  parts[2] 
                        })
                        print("&,&,&", expenses)
        except Exception as e:
            print(f"error reading file: {e}") 

   
# def show_expenses():
#     if not expenses:
#         print("no expenses yet")
#         return
#     print("\nyour expenses: ")


def save_expenses():
    try:
        with open(DATA_FILE,"w") as file:
            for expense in expenses:
                file.write(f"{expense["description"]},{expense["amount"]},{expense["category"]}\n")

    except Exception as e:
        print(f"error saving file: {e}") 



def add_expense(description, amount, category):
    if not description:
        raise ValueError("Description cannot be empty")
    if category not in CATEGORIES:
        raise ValueError("Invalid category")
    if amount <= 0:
        raise ValueError("IAmount must be positive")

    
    expense = {
        "description": description,
        "amount": amount,  
        "category":  category 
        }

    expenses.append(expense)

    save_expenses()


def main():
    load_expenses()
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

                add_expense(description, amount, category)

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