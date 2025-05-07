# Simple To-Do List App

import unicodedata

todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Show Task(s)")
    print("3. Remove Task")
    print("4. Clear Tasks")
    print("5. Save Task(s) to File")
    print("6. Exit")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f'"{task}" added!')

def show_tasks():
    print("\n--- Your Tasks ---")
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    show_tasks()
    try:
        index = int(input("Which task number you would like to remove?: ")) - 1
        removed = todo_list.pop(index)
        print(f'"{removed}" is removed!')
    except(IndexError, ValueError):
        print("The number entered is invalid, please try again. ")

def clear_tasks():
    todo_list.clear()
    print("All tasks cleared!")

def save_tasks():
    with open("my_tasks.txt", "w", encoding="utf-8") as file:
        for i, task in enumerate(todo_list, start=1):
            file.write(f"{i}. {task}\n")
    print('Tasks saved to "my_tasks.txt"')

# Main Loop

while True:
    show_menu()
    choice = input("Please choose an option (1-6): ")
    choice = unicodedata.normalize('NFKC', choice) # handles full-width input

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        save_tasks()
    elif choice == "6":
        save_tasks() # Auto-save when exiting
        print("Goodbye. 頑張ってくださいね！")
        break
    else:
        print("Sorry, invalid option. Please enter 1-6 only.")