class Bank:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def show_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    while True:
        choice = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'q' to quit: ").lower()
        match choice:
            case 'q':
                print("Exiting the bank system.")
                break
            case 'd':
                amount = float(input("Enter amount to deposit: "))
                deposit(amount)
            case 'w':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(amount)
            case 'b':
                show_balance()
            case _:
                print("Invalid choice. Please try again.")