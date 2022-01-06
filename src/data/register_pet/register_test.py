from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet

faker = Faker()


def test_registry():
    """
    Testing registry
    """
    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(user_repository=UserRepositorySpy())
    register_pet = RegisterPet(pet_repository=pet_repo, find_user=find_user)
    attributes = {
        "name": faker.name(),
        "specie": "fish",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }
    response = register_pet.registry(
        name=attributes["name"],
        specie=attributes["specie"],
        user_information=attributes["user_information"],
        age=attributes["age"],
    )
    assert pet_repo.insert_pet_param["name"] == attributes["name"]
    assert pet_repo.insert_pet_param["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_param["age"] == attributes["age"]

    assert (
        find_user.by_id_and_name_param["name"]
        == attributes["user_information"]["user_name"]
    )
    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributes["user_information"]["user_id"]
    )

    assert response["Success"] is True
    assert response["Data"]
