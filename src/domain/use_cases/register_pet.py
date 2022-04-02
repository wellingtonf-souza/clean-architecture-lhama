from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Pets


class RegisterPet(ABC):
    """Interface to register pet"""

    @abstractmethod
    def registry(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """use case"""
        raise NotImplementedError
