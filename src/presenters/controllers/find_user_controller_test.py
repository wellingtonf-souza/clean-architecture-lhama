from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_user_controller import FindUserController
from faker import Faker
from src.data.test import FindUserSpy

faker = Faker()


def test_handle():
    """test hande"""
    find_user_use_case = FindUserSpy(user_repository=UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case=find_user_use_case)
    http_request = HttpRequest(
        query={"user_id": faker.random_number(), "user_name": faker.word()}
    )
    response = find_user_controller.route(http_request=http_request)

    assert (
        find_user_use_case.by_id_and_name_param["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_param["name"]
        == http_request.query["user_name"]
    )

    assert response.status_code == 200
    assert response.body


def test_handle_no_query():
    """test hande"""
    find_user_use_case = FindUserSpy(user_repository=UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case=find_user_use_case)
    http_request = HttpRequest()
    response = find_user_controller.route(http_request=http_request)

    assert find_user_use_case.by_id_and_name_param == {}
    assert find_user_use_case.by_id_param == {}
    assert find_user_use_case.by_name_param == {}

    assert response.status_code == 400
    assert "error" in response.body
