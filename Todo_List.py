"""
Todo List Manager
FIXED: Function name typo and undefined variable reference
"""

tasks = []

def add_task(task):
    """
    Add a new task to the list
    """
    if task and task.strip():
        tasks.append(task.strip())
        print(f"Task Added: {task}")
    else:
        print("Cannot add empty task")

def delete_task(task):  # FIXED: Was 'deletete_task'
    """
    Delete a task from the list
    """
    if task in tasks:
        tasks.remove(task)
        print(f"Task Deleted: {task}")
    else:
        print("Task not found")
    
def view_tasks():  # FIXED: Was 'view_task' without plural
    """
    View all tasks
    """
    if not tasks:
        print("No tasks in the list")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()  # Empty line for better formatting

def main():
    """
    Main program loop
    """
    print("\n=== Todo List Manager ===\n")
    
    while True:
        print("Options:")
        print("  'add'    - Add a task")
        print("  'delete' - Delete a task")
        print("  'view'   - View all tasks")
        print("  'exit'   - Exit program")
        print()

        user_input = input("Choose an option: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        elif user_input == "add":
            task = input("Enter a task: ").strip()
            add_task(task)

        elif user_input == "delete":
            task = input("Enter the task to delete: ").strip()
            delete_task(task)

        elif user_input == "view":
            view_tasks()  # FIXED: No argument needed
        
        else: 
            print("Invalid input. Please choose from: add, delete, view, exit\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")
