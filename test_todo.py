from src.todo_app import TodoApp


def test_todo_functionality():
    """Test all todo functionalities."""
    print("Testing Todo Application functionalities...")

    # Create a new app instance
    app = TodoApp()

    # Test 1: Add Task
    print("\n1. Testing Add Task functionality:")
    task1 = app.add_task("Test Task 1", "This is a test task")
    task2 = app.add_task("Test Task 2", "Another test task")
    print(f"   Added task: {task1}")
    print(f"   Added task: {task2}")
    print(f"   Total tasks: {len(app.get_all_tasks())}")

    # Test 2: View Task List
    print("\n2. Testing View Task List functionality:")
    tasks = app.get_all_tasks()
    for task in tasks:
        print(f"   {task}")

    # Test 3: Update Task
    print("\n3. Testing Update Task functionality:")
    update_success = app.update_task(task1.id, "Updated Task 1", "Updated description")
    print(f"   Update successful: {update_success}")
    if update_success:
        updated_task = app.get_task_by_id(task1.id)
        print(f"   Updated task: {updated_task}")

    # Test 4: Mark as Complete
    print("\n4. Testing Mark as Complete functionality:")
    complete_success = app.mark_task_complete(task1.id)
    print(f"   Mark complete successful: {complete_success}")
    if complete_success:
        completed_task = app.get_task_by_id(task1.id)
        print(f"   Task after marking complete: {completed_task}")

    # Test 5: Mark as Incomplete
    print("\n5. Testing Mark as Incomplete functionality:")
    incomplete_success = app.mark_task_incomplete(task1.id)
    print(f"   Mark incomplete successful: {incomplete_success}")
    if incomplete_success:
        incomplete_task = app.get_task_by_id(task1.id)
        print(f"   Task after marking incomplete: {incomplete_task}")

    # Test 6: Delete Task
    print("\n6. Testing Delete Task functionality:")
    print(f"   Before deletion - Total tasks: {len(app.get_all_tasks())}")
    delete_success = app.delete_task(task2.id)
    print(f"   Delete successful: {delete_success}")
    print(f"   After deletion - Total tasks: {len(app.get_all_tasks())}")

    # Final view to confirm changes
    print("\n7. Final task list:")
    final_tasks = app.get_all_tasks()
    for task in final_tasks:
        print(f"   {task}")

    print("\nAll functionality tests completed successfully!")


if __name__ == "__main__":
    test_todo_functionality()