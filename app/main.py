from banking import Account, deposit, withdraw, transfer, AccountNotFound, InsufficientFunds

def print_menu():
    print("\n=== Banking System ===")
    print("1. Create Account")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Accounts")
    print("q. Quit")

def _read_nonempty(prompt: str) -> str:
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input can not be empty.")

def create_account(accounts: list[Account], next_id: list[int]) -> None:
    owner = _read_nonempty("Owner Name: ")
    acct = Account(id=next_id[0], owner=owner, balance=0.0)
    accounts.append(acct)
    print(f"Created Account #{acct.id} for {acct.owner} (balance{acct.balance:.2f})")
    next_id[0] += 1








def handle_choice(choice: str, accounts: list[Account], next_id: list[int]):
    if choice == "1":
        create_account(accounts, next_id)
    elif choice == "2":
        print("[TODO] deposit")
    elif choice == "3":
        print("[TODO] withdraw")
    elif choice == "4":
        print("[TODO] transfer")
    elif choice == "5":
        if not accounts:
            print("No accounts.")
        else:
            print("\nID   | Owner               | Balance")
            print("-----------------------------------")
            for a in accounts:
                print(f"{a.id:<3} | {a.owner:<20} | {a.balance:>8.2f}")
    elif choice == "q":
        print("Goodbye!")
        raise SystemExit
    else:
        print("Invalid choice.")

    
def main():
    accounts: list[Account] = []
    next_id = [1]
    while True:
        print_menu()
        choice = input("choice: ").strip().lower()
        handle_choice(choice, accounts, next_id)


if __name__ == "__main__":
    main()