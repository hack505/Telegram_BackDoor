import os
import json
from datetime import datetime
from colorama import init, Fore, Style
from cursor import hide, show

init(autoreset=True)  # Initialize colorama


def edit_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print("\nEdit Task:")
        print(f"1. Edit Title (Current: {task['title']})")
        print(f"2. Edit Due Date (Current: {task['due_date']})")
        print(
            f"3. Mark as Incomplete" if task['completed'] else f"3. Mark as Completed")
        print("4. Cancel")

        edit_choice = input("Enter your edit choice (1-4): ")

        if edit_choice == '1':
            new_title = input("Enter new title: ")
            task['title'] = new_title
            save_tasks(tasks)
            print("Title updated successfully.")
        elif edit_choice == '2':
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            task['due_date'] = new_due_date
            save_tasks(tasks)
            print("Due date updated successfully.")
        elif edit_choice == '3':
            task['completed'] = not task['completed']
            save_tasks(tasks)
            print("Task status updated successfully.")
        elif edit_choice == '4':
            print("Edit canceled.")
        else:
            print("Invalid edit choice.")
    else:
        print("Invalid task index.")


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title, due_date):
    task = {'title': title, 'due_date': due_date, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f'{Fore.GREEN}Task "{title}" added successfully!{Style.RESET_ALL}')


def view_tasks(tasks):
    if not tasks:
        print(f'{Fore.YELLOW}No tasks available.{Style.RESET_ALL}')
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            status = f'{Fore.GREEN}[X]{Style.RESET_ALL}' if task['completed'] else f'{Fore.RED}[ ]{Style.RESET_ALL}'
            print(f"{idx}. {status} {task['title']} (Due: {task['due_date']})")


def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        save_tasks(tasks)
        print(f'{Fore.GREEN}Task marked as completed.{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Invalid task index.{Style.RESET_ALL}')


def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(
            f'{Fore.GREEN}Task "{deleted_task["title"]}" deleted successfully.{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Invalid task index.{Style.RESET_ALL}')


init(autoreset=True)  # Initialize colorama

# ... (Rest of the code remains unchanged)


def main():
    hide()  # Hide the cursor
    tasks = load_tasks()

    while True:
        os.system('clear')  # Clear the terminal screen
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, due_date)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = int(
                input("Enter the task index to mark as completed: "))
            mark_completed(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            delete_task(tasks, task_index)
        elif choice == '6':
            break
        elif choice == '5':
            task_index = int(input("Enter the task index to edit: "))
            edit_task(tasks, task_index)

        else:
            print(
                f'{Fore.RED}Invalid choice. Please enter a choice between 1 and 5.{Style.RESET_ALL}')

        # Wait for user input before clearing the screen
        input("Press Enter to continue...")

    show()  # Show the cursor


if __name__ == "__main__":
    main()
