from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository
from src.data.register_pet import RegisterPet
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """Register pet route"""
    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterPet(repository, find_user_use_case)
    register_pet_route = RegisterPetController(use_case)
    return register_pet_route
