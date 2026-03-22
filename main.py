from sysinfo import show_sysinfo as show_sysinfo
from logcheck import check_log as check_log
from tasklist import manage_tasks as manage_tasks

def show_menu():
    """
    Show main menu
    This function prints main menu
    """

    menu = """
1. System Info
2. Log Checker
3. Task List
0. Exit
"""
    print(menu)


def main():
    is_main_menu_on = True

    while is_main_menu_on:
        """
        Main menu logic

        This function prints main menu,
        takes a choice from the user,
        runs the coresponding module
        """
        show_menu()

        user_choice = int(input("Enter choice then press enter: "))

        if user_choice == 1:
            show_sysinfo()
        if user_choice == 2:
            check_log()
        if user_choice == 3:
            manage_tasks()
        if user_choice == 0:
            print("See you soon...")
            is_main_menu_on = False

main()
