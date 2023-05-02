# Use the input() function to prompt the user to enter a task name and due date.
# Store the task name and due date in a list or dictionary.
# Use a loop to display all the tasks in the list, along with their due dates.
# Add the ability to delete a task by entering its index number.
# Add the ability to edit a task name or due date by entering its index number.

# Bonus:
# Add the ability to search for tasks by name or due date.
# Allow the user to mark a task as completed by entering its index number.

import datetime

tasks = []


def display_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['name']} (Due {task['due_date']}) {'(Completed)' if task['completed'] else ''}")


def add_task():
    name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    task = {'name': name, 'due_date': due_date, 'completed': False}
    tasks.append(task)
    print("Task added successfully.")


def mark_task_completed():
    task_num = int(input("Enter task number to mark as completed: "))
    tasks[task_num - 1]['completed'] = True
    print("Task marked as completed.")


def delete_task():
    task_num = int(input("Enter task number to delete: "))
    del tasks[task_num - 1]
    print("Task deleted.")


def search_tasks():
    query = input("Enter search query: ")
    found_tasks = [task for task in tasks if query in task['name'] or query in task['due_date']]
    if len(found_tasks) == 0:
        print("No matching tasks found.")
    else:
        print("Matching tasks:")
        for i, task in enumerate(found_tasks):
            print(f"{i + 1}. {task['name']} (Due {task['due_date']}) {'(Completed)' if task['completed'] else ''}")


def edit_task():
    task_num = int(input("Enter task number to edit: "))
    task = tasks[task_num - 1]
    print(f"Editing task {task['name']}:")
    new_name = input("Enter new name (leave blank to keep current name): ")
    if new_name != "":
        task['name'] = new_name
    new_due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current due date): ")
    if new_due_date != "":
        task['due_date'] = new_due_date
    print("Task edited successfully.")


def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Search task")
        print("6. QUIT")
        option = int(input('Enter your choice: '))
        if option == 1:
            add_task()
        elif option == 2:
            display_tasks()
        elif option == 3:
            mark_task_completed()
        elif option == 4:
            delete_task()
        elif option == 5:
            search_tasks()
        elif option == 6:
            print('Exiting task list!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')

main()
