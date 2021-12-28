from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to register user"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """case"""
        raise NotImplementedError
