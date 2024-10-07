from task import Task
from task_storage import save_tasks, load_tasks, delete_task
from utils import get_valid_input, get_date_input


def main_menu():
    print("\nTask Manager\n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Filter Tasks")
    print("7. Exit")


def add_task(tasks):
    title = get_valid_input("Enter task title: ")
    description = get_valid_input("Enter task description: ")
    due_date = get_date_input("Enter due date (MM/DD/YYYY) or leave blank: ")
    category = get_valid_input("Enter category or leave blank: ", optional=True)

    task = Task(title, description, due_date, category)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    # Ask user how they want to sort the tasks
    sort_option = input("Sort tasks by: \n1. Due Date \n2. Completion Status \n3. No Sorting \nChoose an option: ")
    
    if sort_option == '1':
        tasks.sort(key=lambda task: (task.due_date is None, task.due_date))
    elif sort_option == '2':
        tasks.sort(key=lambda task: task.completed)

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def edit_task(tasks):
    task_title = get_valid_input("Enter the title of the task to edit: ")
    
    task_to_edit = next((task for task in tasks if tasks.title == task_title), None)

    if not task_to_edit:
            print(f"No task found with the title '{task_title}'.")
            return
    
    print(f"Editing Task: {task_to_edit}")

    new_title = get_valid_input(f"Enter new title or leave blank to keep '{task_to_edit.title}': ", optional=True)
    new_description = get_valid_input(f"Enter new description or leave blank to keep '{task_to_edit.description}': ", optional=True)
    new_due_date = get_date_input(f"Enter new due date (YYYY-MM-DD) or leave blank to keep '{task_to_edit.due_date}': ")
    new_category = get_valid_input(f"Enter new category or leave blank to keep '{task_to_edit.category}': ", optional=True)

    if not new_title and not new_description and not new_due_date and not new_category:
        print("No changes have been made. Task was not updated.")
        return

    #Update the task only if new values are provided
    task_to_edit.title = new_title if new_title else task_to_edit.title
    task_to_edit.description = new_description if new_description else task_to_edit.description
    task_to_edit.due_date = new_due_date if new_due_date else task_to_edit.due_date
    task_to_edit.category = new_category if new_category else task_to_edit.category

    save_tasks(tasks)
    print(f"Task '{task_title}' has been updated!")
         

def filter_tasks(tasks):
    if not tasks:
        print("No tasks available to filter.")
        return
    
    filter_option = input("Filter by: \n1. Category \n2. Due Date \nChoose an option: ")

    if filter_option == '1':
        category = get_valid_input("Enter category to filter by: ")
        filtered_tasks = [task for task in tasks if task.category == category]
        if filtered_tasks:
            for i, task in enumerate(filtered_tasks, start=1):
                print(f"{i}. {task}")
        else:
            print(f"No tasks found for category '{category}'.")

    elif filter_option == '2':
        due_date = get_date_input("Enter due date(YYYY-MM-DD) to filter by: ")

        if due_date:
            filtered_tasks = [task for task in tasks if task.due_date == due_date]
            
            if filtered_tasks:
                for i, task in enumerate(filtered_tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print(f"No tasks found with due date '{due_date}'.")
        else:
            print("Invalid due date provided.")
    else:
        print("Invalid filter option selected.")


def complete_task(tasks):
    task_title = get_valid_input("Enter the title of the task to mark complete: ")
    for task in tasks:
        if task.title == task_title:
            task.mark_completed()
            save_tasks(tasks)
            print(f"Task '{task_title}' marked as complete!")
            return
    print(f"No task found with title '{task_title}'.")


def delete_task_from_list(tasks):
    task_title = get_valid_input("Enter the title of the task to delete: ")
    tasks = delete_task(tasks, task_title)
    save_tasks(tasks)
    print(f"Task '{task_title}' deleted!")


def main():
    tasks = load_tasks()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task_from_list(tasks)
        elif choice == '5':
            edit_task(tasks)
        elif choice == '6':
            filter_tasks(tasks)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again!")


if __name__ == "__main__":
    main()
