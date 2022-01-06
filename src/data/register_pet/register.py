from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.domain.models import Pets, Users
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import RegisterPet as RegisterPetInterface


class RegisterPet(RegisterPetInterface):
    """Class to define use case register pet"""

    def __init__(
        self, pet_repository: Type[PetRepository], find_user: Type[FindUser]
    ) -> None:
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """
        Register pet
        :param - name:
               - specie:
               - age:
               - user_information: Dict with user_id and/or user_name
        :return - Dict with informations of the process
        """
        response = None
        validate_entry = (
            isinstance(name, str)
            and isinstance(specie, str)
            and isinstance(age, (int, type(None)))
        )
        user = self.__find_user_information(user_information=user_information)
        checker = validate_entry and user["Success"]
        if checker:
            response = self.pet_repository.insert_pet(
                name=name, specie=specie, age=age, user_id=user_information["user_id"]
            )
        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """
        Check user
        :param - user_information
        :return - Dict
        """
        user_founded = None
        user_params = user_information.keys()
        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_id=user_information["user_id"], name=user_information["user_name"]
            )
        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(name=user_information["user_name"])
        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_id=user_information["user_id"])
        else:
            return {"Success": False, "Data": None}
        return user_founded
