from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_by_id():
    """Testing by_id method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repository=user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])
    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id():
    """Testing by_id fail method in FindUser"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"id": faker.word()}
    response = find_user.by_id(user_id=attribute["id"])
    assert not user_repo.select_user_params
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """Testing by_name method in FindUser"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"name": faker.word()}
    response = find_user.by_name(name=attribute["name"])
    assert user_repo.select_user_params["name"] == attribute["name"]
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_name():
    """Testing by_name fail method in FindUser"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attribute = {"name": faker.random_number(digits=2)}
    response = find_user.by_name(name=attribute["name"])
    assert not user_repo.select_user_params
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """Testing by_id_and_name method in FindUser"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)
    attribute = {"user_id": faker.random_number(digits=2), "name": faker.word()}
    response = find_user.by_id_and_name(
        user_id=attribute["user_id"], name=attribute["name"]
    )
    assert user_repo.select_user_params["user_id"] == attribute["user_id"]
    assert user_repo.select_user_params["name"] == attribute["name"]
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_id_and_name():
    """Testing by_id_and_name fail method in FindUser"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)
    attribute = {
        "user_id": faker.random_number(digits=2),
        "name": faker.random_number(digits=2),
    }
    response = find_user.by_id_and_name(
        user_id=attribute["user_id"], name=attribute["name"]
    )
    assert user_repo.select_user_params == {}
    assert response["Success"] is False
    assert response["Data"] is None
