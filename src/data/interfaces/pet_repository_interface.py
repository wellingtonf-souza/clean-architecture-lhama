from abc import abstractmethod, ABC
from typing import List
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    """Interface Pet"""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Abstract method"""
        raise NotImplementedError

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Abstract method"""
        raise NotImplementedError
