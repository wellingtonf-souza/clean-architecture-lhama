from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """
    Compose
    :param - None
    :return - Object with Register User Route
    """
    repository = UserRepository()
    use_case = RegisterUser(repository)
    return RegisterUserController(use_case)
