"""
Text-Based Banking & Utility System

Beginner capstone project demonstrating fundamentals:
- Python syntax, variables, data types, casting, numbers, strings, booleans
- Operators, conditionals, loops (for/while), functions, range

Run this script in a console and follow the prompts.
"""

# ---------------------------------------------------------------------------
# helper functions implementing core features
# ---------------------------------------------------------------------------

def get_user_info():
    """Ask the user for their name and starting balance.

    Demonstrates: input(), casting, strings, floats, validation with booleans.
    """
    # Python Variables and Data Types
    name = input("Enter your name: ")  # str

    while True:
        balance_str = input("Enter starting balance (e.g. 100.50): ")
        try:
            # Python Casting: string -> float
            balance = float(balance_str)
            break
        except ValueError:
            print("Please provide a valid number.")
    return name, balance


def display_menu():
    """Show the main menu options and return the user's choice.

    Demonstrates: printing strings, booleans, operators with comparison.
    """
    print("\n=== Main Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction Summary")
    print("5. Generate Interest Projection")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    return choice


def deposit(balance, transactions):
    """Perform a deposit and return the new balance.

    Demonstrates: numbers, operators, conditionals, functions.
    """
    amount_str = input("Enter amount to deposit: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid number. Deposit cancelled.")
        return balance

    if amount <= 0:
        print("Amount must be positive.")
    else:
        balance += amount
        transactions.append(("deposit", amount))
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
    return balance


def withdraw(balance, transactions):
    """Withdraw funds if sufficient balance is available.

    Demonstrates: booleans, operators, if/else.
    """
    amount_str = input("Enter amount to withdraw: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid number. Withdrawal cancelled.")
        return balance

    if amount <= 0:
        print("Amount must be positive.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        transactions.append(("withdraw", amount))
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    return balance


def summary(transactions):
    """Print a summary of the transactions list.

    Demonstrates: for loops, range, counting.
    """
    deposits = 0
    withdrawals = 0
    total_dep = 0.0
    total_wit = 0.0

    for ttype, amt in transactions:
        if ttype == "deposit":
            deposits += 1
            total_dep += amt
        else:
            withdrawals += 1
            total_wit += amt

    print("\n--- Transaction Summary ---")
    print(f"Deposits: {deposits} totalling ${total_dep:.2f}")
    print(f"Withdrawals: {withdrawals} totalling ${total_wit:.2f}")


def interest_projection(balance):
    """Show projected balance for N months at a fixed interest rate.

    Demonstrates: for loops, range, arithmetic operators.
    """
    rate = 0.02  # 2% monthly interest (example)
    months_str = input("How many months to project? ")
    try:
        months = int(months_str)
    except ValueError:
        print("Invalid number of months.")
        return

    print("\nMonth  Balance")
    for m in range(1, months + 1):
        balance = balance + (balance * rate)
        print(f"{m:5d}  ${balance:.2f}")


def confirm_exit():
    """Ask the user to confirm exit.

    Demonstrates: strings, boolean comparison.
    """
    ans = input("Are you sure you want to exit? (y/n): ")
    return ans.lower() in ("y", "yes")


# ---------------------------------------------------------------------------
# main loop
# ---------------------------------------------------------------------------

def main():
    name, balance = get_user_info()
    transactions = []  # list of tuples (type, amount)

    while True:  # while loop for the menu
        choice = display_menu()

        if choice == "1":
            print(f"\n{name}, your current balance is: ${balance:.2f}")
        elif choice == "2":
            balance = deposit(balance, transactions)
        elif choice == "3":
            balance = withdraw(balance, transactions)
        elif choice == "4":
            summary(transactions)
        elif choice == "5":
            interest_projection(balance)
        elif choice == "6":
            if confirm_exit():
                print("Goodbye!")
                break
        else:
            print("Invalid option; please choose 1-6.")


if __name__ == "__main__":
    main()