from typing import NamedTuple

Pets = NamedTuple(
    "Pets",
    [("id", int), ("name", str), ("specie", str), ("age", int), ("user_id", int)],
)
