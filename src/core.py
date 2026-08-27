# Mustapha
# core.py

import os
import database
from typing import Any

yellow = "\033[33m"
white  = "\033[97m"
reset  = "\033[0m"


def get_string(txt: str) -> str:
    while True:
        s = input(f"{yellow}{txt}{reset}").strip()
        if not s:
            print(f"{white}\nEmpty input is not supported, please re-enter{reset}")
            continue
        return s


def get_int(txt: str, min_range: int, max_range: int) -> int:
    while True:
        try:
            num = int(input(f"{yellow}{txt}{reset}"))
            if num > max_range or num < min_range:
                print(f"\n{white}Input range is undefined, please re-enter{reset}")
                continue
            return num
        except ValueError:
            print(f"\n{white}Input is invalid, please re-enter{reset}")


def show_menu() -> None:
    print(f"\n{yellow}------------------The Program Menu------------------{reset}\n")
    print(f"{white}1.{reset} {yellow}Show users{white}")
    print(f"{white}2.{reset} {yellow}Add a user{white}")
    print(f"{white}3.{reset} {yellow}Del a user{white}")
    print(f"{white}4.{reset} {yellow}Sort by age{white}")
    print(f"{white}5.{reset} {yellow}Reverse sort by age{white}")
    print(f"{white}6.{reset} {yellow}Get available users number{white}")
    print(f"{white}7.{reset} {yellow}Sort by name{white}")
    print(f"{white}8.{reset} {yellow}Reverse sort by name{white}")
    print(f"{white}9.{reset} {yellow}Calculate average ages{white}")
    print(f"{white}10.{reset} {yellow}Calculate Minimum & Maximum ages{white}")
    print(f"{white}0.{reset} {yellow}Exit program{white}\n")


def add_user() -> None:
    os.system("clear")
    name  = get_string("Enter name: ")
    job   = get_string("Enter job: ")
    age   = get_int("Enter age: ", 10, 99)
    email = get_string("Enter e-mail: ")

    new: database.User = {"name": name, "job": job, "age": age, "email": email}
    database.add_list(new)

    print(f"{yellow}\nUser added to list{reset}")
    input(f"{white}Press a key to continue . . .{reset}")


def del_user() -> None:
    os.system("clear")
    name = get_string("Enter name of user that you want to delete it: ")
    age = get_int("Enter age of user that you want to delete it: ", 10, 99)
    result = database.del_list(name, age)

    if result == 0:
        print(f"{yellow}\nThe user deleted successfully!{reset}")
    else:
        print(f"{yellow}\nCould not find user with this info!{reset}")
    input(f"{white}Press a key to continue . . .{reset}")


def show_users() -> None:
    os.system("clear")
    print(f"{white}Registered users list{reset}\n")

    if not database.users:
        print(f"{yellow}Users list is empty!{reset}")
        input(f"{white}Press a key to continue . . .{reset}")
        return

    for x in database.users:
        print(f"{white}Name:{reset} {yellow}{x['name']}{reset}")
        print(f"{white}Job:{reset} {yellow}{x['job']}{reset}")
        print(f"{white}Age:{reset} {yellow}{x['age']} years old{reset}")
        print(f"{white}E-mail:{reset} {yellow}{x['email']}{reset}\n")
    input(f"{white}Press enter to continue . . .{reset}")


def calc_average_age() -> None:
    if not database.users:
        print(f"{yellow}\nUsers list is empty!{reset}")
        input(f"{white}Press a key to continue . . .{reset}")
        return

    total = sum(x["age"] for x in database.users)
    count = len(database.users)
    ave = total / count
    print(f"\n{yellow}Ages average:{reset} {white}{ave}{reset}")
    input(f"{yellow}Press a key to continue . . .{reset}")


def calc_age_range() -> None:
    if not database.users:
        print(f"{yellow}\nUsers list is empty!{reset}")
        input(f"{white}Press a key to continue . . .{reset}")
        return

    min_age = min(x["age"] for x in database.users)
    max_age = max(x["age"] for x in database.users)
    print(f"{white}\nMin:{reset} {yellow}{min_age}{reset}, {white}Max:{reset} {yellow}{max_age}{reset}")
    input(f"{yellow}Press a key to continue . . .{reset}")

