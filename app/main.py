from banking import Account, deposit, transfer, AccountNotFound, InsufficientFunds

def print_menu():
    print("\n=== Banking System ===")
    print("1. Create Account")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View Accounts")
    print("q. Quit")


def handle_choice(choice: str, account: list[Account], next_id: list[int]):
    if choice == "1":
        print("[TODO] create account")
    elif choice == "2":
        print("[TODO] deposit")
    elif choice == "3":
        print("[TODO] withdraw")
    elif choice == "4":
        print("[TODO] transfer")
    elif choice == "5":
        print("[TODO] view accounts")
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