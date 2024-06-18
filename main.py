# Scripts by BingleyPro
import json

# Setup tasks for to-do list
tasks = []

# -- To-Do List Functions ---
def add_task(title, desc=""):
    tasks.append({"title": title, "desc": desc, "completed": False})

def list_tasks():
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['title']} - {task['desc']} - {'Completed' if task['completed'] else 'Not Completed'}")

def complete_task(index):
    tasks[index]["completed"] = True

def remove_task(index):
    tasks.pop(index)

def save_tasks_to_file(filename):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def load_tasks_from_file(filename):
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file.")

# -- Calculator Functions --
def get_percentage_of(value, percentage):
    return value * percentage / 100

# Calculate value before applying percentage
def backwards_get_percentage_of(value, percentage):
    return (value * percentage) / (percentage + 1)

def addition(value1, value2):
    return value1 + value2

def subtraction(value1, value2):
    return value1 - value2

def multiplication(value1, value2):
    return value1 * value2

def division(value1, value2):
    return value1 / value2

# Main Script
def show_menu():
    load_tasks_from_file("tasks.json")

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            add_task(title, description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: "))
            complete_task(index)
        elif choice == "4":
            index = int(input("Enter task index to remove: "))
            remove_task(index)
        elif choice == "5":
            save_tasks_to_file("tasks.json")
            print("Tasks saved.")
        elif choice == "6":
            save_tasks_to_file("tasks.json") 
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Main program loop
if __name__ == "__main__":
    show_menu()