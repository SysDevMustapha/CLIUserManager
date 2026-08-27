# Mustapha
# loop.py

import os
import core
import database


def loop() -> None:
    is_running = True
    database.read_data()

    while is_running:
        os.system("clear")
        core.show_menu()
        choice = core.get_int(f"{core.white}Enter choice: {core.reset}", 0, 10)

        match choice:
            case 0:
                is_running = False
                print(f"{core.yellow}Thanks for using my program, Mustapha :){core.white}")
            case 1:
                core.show_users()
            case 2:
                core.add_user()
            case 3:
                core.del_user()
            case 4:
                database.sort_by_age(True)
                input(f"{core.yellow}Sorted! press a key to continue . . .{core.reset}")
            case 5:
                database.sort_by_age(False)
                input(f"{core.yellow}Sorted! press a key to continue . . .{core.reset}")
            case 6:
                print(f"{core.white}\nNumber of available users: {database.get_users_num()}{core.reset}")
                input(f"{core.yellow}Press a key to continue . . .{core.reset}")
            case 7:
                database.sort_by_name(True)
                input(f"{core.yellow}Sorted! press a key to continue . . .{core.reset}")
            case 8:
                database.sort_by_name(False)
                input(f"{core.yellow}Sorted! press a key to continue . . .{core.reset}")
            case 9:
                core.calc_average_age()
            case 10:
                core.calc_age_range()

    database.write_data()
