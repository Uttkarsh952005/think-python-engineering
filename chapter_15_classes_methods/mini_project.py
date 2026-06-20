"""
Chapter 15: Mini Project - Bank Account Object
Demonstrates encapsulation, state management, and clear interfaces.
"""

class BankAccount:
    """A simple bank account demonstrating method encapsulation."""
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: ${initial_balance:.2f}")

    def __str__(self) -> str:
        return f"Account({self.owner}, Balance: ${self.balance:.2f})"

    def deposit(self, amount: float) -> None:
        """Adds money to the account."""
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
            
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount:.2f}")
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> bool:
        """Removes money if sufficient funds exist."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
            
        if amount > self.balance:
            print(f"Denied: Insufficient funds. Balance is ${self.balance:.2f}")
            return False
            
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount:.2f}")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True

    def print_statement(self) -> None:
        """Prints the transaction history."""
        print(f"\n--- Statement for {self.owner} ---")
        for t in self.transactions:
            print(t)
        print(f"Current Balance: ${self.balance:.2f}\n")

def main():
    print("--- Bank Interface ---")
    account = BankAccount("Alice", 100.0)
    print(account)
    
    account.deposit(50.0)
    account.withdraw(20.0)
    account.withdraw(500.0) # Should fail
    
    account.print_statement()

if __name__ == "__main__":
    main()
