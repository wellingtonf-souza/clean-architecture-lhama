from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Testing registry method"""
    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)
    attribute = {"name": faker.name(), "password": faker.password()}
    response = register_user.register(
        name=attribute["name"], password=attribute["password"]
    )
    assert user_repository.insert_user_params["name"] == attribute["name"]
    assert user_repository.insert_user_params["password"] == attribute["password"]
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Testing registry method"""
    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)
    attribute = {"name": faker.random_number(), "password": faker.password()}
    response = register_user.register(
        name=attribute["name"], password=attribute["password"]
    )
    assert user_repository.insert_user_params == {}
    assert response["Success"] is False
    assert response["Data"] is None
