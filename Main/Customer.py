

from Main.Transaction import User


class Customer(User):
    
    def __init__(self, user_id: str, name: str, email: str, account_balance: float = 0.0):
        super().__init__(user_id, name, email)
        self.account_balance = account_balance
    
