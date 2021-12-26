from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository

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
