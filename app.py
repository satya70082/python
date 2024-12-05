import sys
from datetime import datetime

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nTasks in your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' has been added.")

# Function to delete a task
def delete_task(tasks, task_num):
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the program
def main():
    tasks = []
    
    # Read the arguments passed in Jenkins
    if len(sys.argv) < 2:
        print("No action provided, exiting program.")
        return
    
    action = sys.argv[1]
    
    if action == 'view':
        view_tasks(tasks)
    elif action == 'add' and len(sys.argv) > 2:
        add_task(tasks, sys.argv[2])
    elif action == 'delete' and len(sys.argv) > 2:
        delete_task(tasks, sys.argv[2])
    else:
        print("Invalid arguments provided.")

if __name__ == "__main__":
    main()
