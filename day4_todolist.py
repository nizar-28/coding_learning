# Simple To-Do List App

import unicodedata
todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Clear all tasks")
    print("5. Save tasks to file")
    print("6. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f'"{task}" added!')

def view_tasks():
    print("\n--- Your Tasks ---")
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        removed = todo_list.pop(index)
        print(f'"{removed}" removed!')
    except (IndexError, ValueError):
        print("Invalid number. Please try again.")

def clear_tasks():
    todo_list.clear()
    print("All tasks cleared!")

def auto_save_on_exit():
    with open("my_tasks.txt", "w", encoding="utf-8") as file:
        for i, task in enumerate(todo_list, start=1):
            file.write(f"{i}. {task}\n")
    print("Tasks saved to 'my_tasks.txt'")

# Main Loop
while True:
    show_menu()
    choice = input("Choose and option (1-6): ")
    choice = unicodedata.normalize('NFKC', choice) # handles full-width input

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        auto_save_on_exit()
    elif choice == "6":
        auto_save_on_exit() # Auto-save when exiting
        print("Goodbye! 頑張ってください！")
        break
    else:
        print("Invalid option. Please enter 1-6.")

# Notes:

# Append mode - add tasks to file without erasing. just use "a" instead of "w" at with open.

# Auto-Save on Exit - just add save_tasks() in elif choice == "6"