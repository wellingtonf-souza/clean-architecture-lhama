from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy
from .register_pet_controller import RegisterPetController
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_route():
    """Teste route"""
    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributer = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }
    response = register_pet_route.route(HttpRequest(body=attributer))
    assert register_pet_use_case.registry_param["name"] == attributer["name"]
    assert register_pet_use_case.registry_param["specie"] == attributer["specie"]
    assert register_pet_use_case.registry_param["age"] == attributer["age"]
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributer["user_information"]
    )

    assert response.status_code == 200


def test_route_without_age():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)
    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] is None
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_user_id_in_user_information():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "user_information": {"user_name": faker.word()},
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] is None
    assert (
        register_pet_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_no_body():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)

    response = register_pet_router.route(HttpRequest())

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_body():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {
        "specie": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_wrong_user_information():
    """Testing route method in RegisterUserRouter"""

    register_pet_use_case = RegisterPetSpy(PetRepositorySpy(), None)
    register_pet_router = RegisterPetController(register_pet_use_case)

    attributes = {"name": faker.word(), "specie": "Dog", "user_information": {}}

    response = register_pet_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_pet_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
