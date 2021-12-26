from typing import NamedTuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class UserRepository:
    """Class UserRepository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """
        Insert data in user entity
        :param - name: person name
               - password: user password
        :return - Tuple with new user inserted
        """
        insertData = NamedTuple(
            "Users", [("id", int), ("name", str), ("password", str)]
        )
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return insertData(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
            return None
