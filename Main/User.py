from abc import ABC, abstractmethod


class User(ABC):
    
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
    
    @abstractmethod
    def get_role(self) -> str:
        pass
    
    @abstractmethod
    def perform_action(self):
        pass

