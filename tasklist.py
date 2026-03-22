
tasks = [
    {"task_num": 1, "task_title": "Kaki", "task_content": "Maki sushi"},
    {"task_num": 2, "task_title": "Kaki", "task_content": "Maki sushi"}
]
    
def show_tasks_menu():
    """
    Print tasks operations menu, take a user choice. 
    """
    menu = """
1. Add a new task
2. View all tasks
3. Remove a task by number
4. Return to main menu
"""
    print(menu)
    
    try:
        user_choice = int(input("Enter menu number then press enter: "))
    except ValueError as e:
        print("Invalid choice! Please enter a numeric value.")
        print(e)

    return user_choice

def get_next_task_num():
    next_task_num = len(tasks)+1
    return next_task_num
# print(get_next_task_num())


def new_task():
    new_task = {}
    new_task_title = str(input("Enter a title for the new task\n"))
    new_task_content = str(input("Enter content for the new task\n"))
    new_task_num = get_next_task_num()

    new_task["task_num"] = new_task_num
    new_task["task_title"] = new_task_title
    new_task["task_content"] = new_task_content

    new_task_str = f"""
Review your task and approve
Task title: {new_task_title}
Task content: {new_task_content}

The number for this task will be ({new_task_num})
"""
    print(new_task_str)
    input("Press enter to approve")

    tasks.append(new_task)
# new_task()

def view_all_tasks():
    tasks_str = ""
    for task in tasks:
        cur_title = task["task_title"]
        cur_num = task["task_num"]
        cur_content = task["task_content"]
        title = f"{cur_num}. {cur_title}"
        task_str = f"""

{"=" * len(title)}
{title}
{"=" * len(title)}
{cur_content}
"""     
        tasks_str += task_str
    print(tasks_str)
    return tasks_str
# print(view_all_tasks())

def remove_task_by_number():
    try:
        user_choice = int(input("Enter task number then press enter\n"))
    except ValueError as e:
        print("Invalid choice! Please enter a numeric value.")
        print(e) 

    for task in tasks:
        if task["task_num"] == user_choice:
            del tasks[user_choice - 1]
# remove_task_by_number()
        


def manage_tasks():

    tasks_menu_on = True

    while tasks_menu_on:
        user_choice = show_tasks_menu()

        match user_choice:
            case 1:
                new_task()
            case 2:
                view_all_tasks()
            case 3:
                remove_task_by_number()
            case 4:
                tasks_menu_on = False
