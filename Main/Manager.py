from Main.Transaction import User

class Manager(User):
    
    def __init__(self, user_id: str, name: str, email: str, department: str):
        super().__init__(user_id, name, email)
        self.department = department