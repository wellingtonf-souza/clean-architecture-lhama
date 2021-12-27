from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository
from src.infra.entities import Users as UsersModel

faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should insert user"""
    name = faker.name()
    password = faker.password()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name=name, password=password)
    query_result = engine.execute(
        f"SELECT id, name, password FROM users WHERE id = {new_user.id};"
    ).fetchone()

    engine.execute(f"DELETE FROM users WHERE id = {new_user.id};")
    assert new_user.id == query_result.id
    assert new_user.name == query_result.name
    assert new_user.password == query_result.password


def test_select_user():
    """Test select user"""
    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.password()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, password) VALUES ({user_id},'{name}','{password}');"
    )
    query_user_id = user_repository.select_user(user_id=user_id)
    query_name = user_repository.select_user(name=name)
    query_user_id_and_name = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user_id
    assert data in query_name
    assert data in query_user_id_and_name

    engine.execute(f"DELETE FROM users WHERE id = {user_id}")
