# Quickstart Guide: Console Todo App

## Overview
This guide provides instructions for quickly getting started with the console-based todo application. The app allows users to manage tasks through a menu-driven interface.

## Prerequisites
- Python 3.13+ installed on your system
- UV package manager installed
- Basic command-line interface knowledge

## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:AbdullahSheikh7/giaic-aidd-hackathon-2.git
cd giaic-aidd-hackathon-2
```

### 2. Install Dependencies
```bash
uv sync
```

### 3. Run the Application
```bash
uv run python src/main.py
```

Alternatively, if installed as a package:
```bash
todo-app
```

## First Steps

### 1. Navigate the Main Menu
When you run the application, you'll see the main menu with the following options:
```
==================================================
TODO APPLICATION - MAIN MENU
==================================================
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Mark Task as Incomplete
7. Exit
==================================================
```

### 2. Add Your First Task
1. Select option `1` to add a task
2. Enter a title for your task (required)
3. Enter a description (optional)
4. The system will confirm the task creation with a unique ID

### 3. View Your Tasks
1. Select option `2` to view all tasks
2. All tasks will be displayed with their ID, title, description, and completion status
3. Completed tasks will show with a "✓" indicator, incomplete with "○"

## Common Operations

### Updating a Task
1. Select option `3` to update a task
2. The system will display all tasks for reference
3. Enter the ID of the task you want to update
4. Enter new values for title and description (or press Enter to keep current values)

### Marking Tasks Complete/Incomplete
1. Select option `5` to mark a task complete or option `6` to mark it incomplete
2. The system will display all tasks for reference
3. Enter the ID of the task you want to update
4. The system will confirm the status change

### Deleting a Task
1. Select option `4` to delete a task
2. The system will display all tasks for reference
3. Enter the ID of the task you want to delete
4. Confirm the deletion when prompted

## Tips and Best Practices

### Input Validation
- Task titles must not be empty
- Task IDs must be numeric and correspond to existing tasks
- The system will prompt for corrections if invalid input is provided

### Task Management
- Use descriptive titles to make tasks easily identifiable
- Include detailed descriptions for complex tasks
- Regularly mark completed tasks to keep your list current
- Delete tasks that are no longer relevant

### Performance
- The application maintains all data in memory during the session
- Tasks will be lost when the application is closed (in-memory storage)
- For persistent storage, consider future enhancements to the application

## Troubleshooting

### Common Issues
- **Invalid menu choice**: Ensure you enter a number between 1 and 7
- **Task not found**: Verify the task ID exists in your task list
- **Empty input**: Task titles cannot be empty

### Error Messages
- "Task title cannot be empty!": Provide a title when adding a task
- "Task with ID X not found!": Verify the task ID is correct
- "Please enter a valid task ID (number).": Enter a numeric task ID
- "Invalid choice. Please enter a number between 1 and 7.": Enter a valid menu option

## Next Steps
- Experiment with all menu options to familiarize yourself with the application
- Try creating multiple tasks to see how the system handles task management
- Test error handling by providing invalid inputs to see how the system responds
- Review the source code in `src/todo_app.py` and `src/main.py` to understand the implementation