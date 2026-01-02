from todo_app import TodoApp
import sys


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("TODO APPLICATION - MAIN MENU")
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Mark Task as Incomplete")
    print("7. Exit")
    print("="*50)


def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def add_task_interface(app: TodoApp):
    """Interface for adding a new task."""
    print("\n--- ADD NEW TASK ---")
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return

    description = input("Enter task description (optional): ").strip()

    try:
        task = app.add_task(title, description)
        print(f"Task '{task.title}' added successfully with ID {task.id}!")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks_interface(app: TodoApp):
    """Interface for viewing all tasks."""
    print("\n--- ALL TASKS ---")
    tasks = app.get_all_tasks()

    if not tasks:
        print("No tasks found!")
        return

    for task in tasks:
        print(task)


def update_task_interface(app: TodoApp):
    """Interface for updating a task."""
    print("\n--- UPDATE TASK ---")
    view_tasks_interface(app)

    if not app.get_all_tasks():
        return

    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = app.get_task_by_id(task_id)

        if not task:
            print(f"Task with ID {task_id} not found!")
            return

        print(f"Current title: {task.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        if not new_title:
            new_title = None

        print(f"Current description: {task.description}")
        new_description = input("Enter new description (or press Enter to keep current): ").strip()
        if not new_description:
            new_description = None

        try:
            if app.update_task(task_id, new_title, new_description):
                print(f"Task {task_id} updated successfully!")
            else:
                print(f"Failed to update task {task_id}")
        except ValueError as e:
            print(f"Error: {e}")
    except ValueError:
        print("Please enter a valid task ID (number).")


def delete_task_interface(app: TodoApp):
    """Interface for deleting a task."""
    print("\n--- DELETE TASK ---")
    view_tasks_interface(app)

    if not app.get_all_tasks():
        return

    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        task = app.get_task_by_id(task_id)

        if not task:
            print(f"Task with ID {task_id} not found!")
            return

        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            if app.delete_task(task_id):
                print(f"Task {task_id} deleted successfully!")
            else:
                print(f"Failed to delete task {task_id}")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Please enter a valid task ID (number).")


def mark_complete_interface(app: TodoApp):
    """Interface for marking a task as complete."""
    print("\n--- MARK TASK AS COMPLETE ---")
    view_tasks_interface(app)

    if not app.get_all_tasks():
        return

    try:
        task_id = int(input("Enter the ID of the task to mark as complete: "))
        task = app.get_task_by_id(task_id)

        if not task:
            print(f"Task with ID {task_id} not found!")
            return

        if app.mark_task_complete(task_id):
            print(f"Task {task_id} marked as complete!")
        else:
            print(f"Failed to mark task {task_id} as complete")
    except ValueError:
        print("Please enter a valid task ID (number).")


def mark_incomplete_interface(app: TodoApp):
    """Interface for marking a task as incomplete."""
    print("\n--- MARK TASK AS INCOMPLETE ---")
    view_tasks_interface(app)

    if not app.get_all_tasks():
        return

    try:
        task_id = int(input("Enter the ID of the task to mark as incomplete: "))
        task = app.get_task_by_id(task_id)

        if not task:
            print(f"Task with ID {task_id} not found!")
            return

        if app.mark_task_incomplete(task_id):
            print(f"Task {task_id} marked as incomplete!")
        else:
            print(f"Failed to mark task {task_id} as incomplete")
    except ValueError:
        print("Please enter a valid task ID (number).")


def main():
    """Main function to run the todo application."""
    print("Welcome to the Todo Application!")

    app = TodoApp()

    # Add some sample tasks for demonstration
    try:
        app.add_task("Buy groceries", "Milk, bread, eggs, fruits")
        app.add_task("Finish project report", "Complete the quarterly report for work")
        app.add_task("Call mom", "Check in with mom this weekend")
    except ValueError:
        # In case the sample tasks fail to add, continue anyway
        pass

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task_interface(app)
        elif choice == '2':
            view_tasks_interface(app)
        elif choice == '3':
            update_task_interface(app)
        elif choice == '4':
            delete_task_interface(app)
        elif choice == '5':
            mark_complete_interface(app)
        elif choice == '6':
            mark_incomplete_interface(app)
        elif choice == '7':
            print("Thank you for using the Todo Application. Goodbye!")
            break


if __name__ == "__main__":
    main()