# Mustapha
# database.py

import json
from pathlib import Path
from typing import TypedDict, List

class User(TypedDict):
    name: str
    job: str
    age: int
    email: str


UserDataPath: Path = Path(__file__).parent / "user-data.json"
users: List[User] = []


def read_data() -> None:
    global users
    try:
        with UserDataPath.open("r", encoding="utf-8") as f:
            users = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        users = []


def write_data() -> None:
    with UserDataPath.open("w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def add_list(new: User) -> None:
    users.append(new)


def del_list(name: str, age: int) -> int:
    for x in users:
        if x["name"] == name and x["age"] == age:
            users.remove(x)
            return 0
    return -1


def sort_by_age(how: bool) -> None:
    users.sort(key=lambda x: x["age"], reverse=not how)


def sort_by_name(how: bool) -> None:
    users.sort(key=lambda x: x["name"], reverse=not how)


def get_users_num() -> int:
    return len(users)
