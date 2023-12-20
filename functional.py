from operator import itemgetter, attrgetter
from dataclasses import dataclass
from typing import Callable


@dataclass
class User:
    name: str
    age: int


def get_names(data):
    """
    extracts values of 'name' key from dict
    """
    return map(itemgetter("name"), data)


def get_object_names(data):
    """
    extracts value of name attribute
    """
    return map(attrgetter("name"), data)


def get_field_extractor(data, key_extractor: Callable):
    return map(key_extractor, data)


if __name__ == "__main__":
    users_objects = [User(name="Paul", age=28), User(name="Liz", age=18)]

    users = [
        {"name": "Paul", "age": 28},
        {"name": "Liz", "age": 18},
    ]

    assert list(get_names(users)) == ["Paul", "Liz"]
    assert list(get_object_names(users_objects)) == ["Paul", "Liz"]

    get_names_dict = get_field_extractor(users, itemgetter("name"))
    assert list(get_names_dict) == ["Paul", "Liz"]

    get_names_object = get_field_extractor(users_objects, attrgetter("name"))
    assert list(get_names_object) == ["Paul", "Liz"]
