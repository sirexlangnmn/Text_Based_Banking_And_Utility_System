"""
Text-Based Banking & Utility System (Refactored)

Demonstrates:
- Python fundamentals
- DRY, SOLID, KISS principles
- Readable, testable, maintainable structure
"""

from typing import List, Tuple

Transaction = Tuple[str, float]
MONTHLY_INTEREST_RATE = 0.02


# ---------------------------------------------------------------------------
# Input utilities (DRY)
# ---------------------------------------------------------------------------

def get_string(prompt: str) -> str:
    return input(prompt).strip()


def get_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive number.")


def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive whole number.")


# ---------------------------------------------------------------------------
# Core banking logic (Business Rules)
# ---------------------------------------------------------------------------

def deposit(balance: float, amount: float) -> float:
    return balance + amount


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount


def calculate_interest(balance: float, months: int) -> List[float]:
    projections = []
    for _ in range(months):
        balance += balance * MONTHLY_INTEREST_RATE
        projections.append(balance)
    return projections


# ---------------------------------------------------------------------------
# Presentation / Output
# ---------------------------------------------------------------------------

def display_menu() -> str:
    print("\n=== Main Menu ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Transaction Summary")
    print("5. Generate Interest Projection")
    print("6. Exit")
    return get_string("Choose an option (1-6): ")


def show_summary(transactions: List[Transaction]) -> None:
    deposits = [amt for t, amt in transactions if t == "deposit"]
    withdrawals = [amt for t, amt in transactions if t == "withdraw"]

    print("\n--- Transaction Summary ---")
    print(f"Deposits: {len(deposits)} totalling ${sum(deposits):.2f}")
    print(f"Withdrawals: {len(withdrawals)} totalling ${sum(withdrawals):.2f}")


def confirm_exit() -> bool:
    return get_string("Are you sure you want to exit? (y/n): ").lower() in {"y", "yes"}


# ---------------------------------------------------------------------------
# Application flow (Controller)
# ---------------------------------------------------------------------------

def main() -> None:
    name = get_string("Enter your name: ")
    balance = get_float("Enter starting balance: ")
    transactions: List[Transaction] = []

    while True:
        choice = display_menu()

        if choice == "1":
            print(f"\n{name}, your current balance is ${balance:.2f}")

        elif choice == "2":
            amount = get_float("Enter amount to deposit: ")
            balance = deposit(balance, amount)
            transactions.append(("deposit", amount))
            print(f"Deposited ${amount:.2f}")

        elif choice == "3":
            amount = get_float("Enter amount to withdraw: ")
            try:
                balance = withdraw(balance, amount)
                transactions.append(("withdraw", amount))
                print(f"Withdrew ${amount:.2f}")
            except ValueError as e:
                print(e)

        elif choice == "4":
            show_summary(transactions)

        elif choice == "5":
            months = get_int("How many months to project? ")
            projections = calculate_interest(balance, months)
            print("\nMonth  Balance")
            for i, value in enumerate(projections, start=1):
                print(f"{i:5d}  ${value:.2f}")

        elif choice == "6":
            if confirm_exit():
                print("Goodbye!")
                break

        else:
            print("Invalid option. Please choose 1–6.")


if __name__ == "__main__":
    main()