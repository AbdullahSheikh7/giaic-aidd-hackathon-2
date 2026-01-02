# Interface Contracts: Console Todo App

## Overview
This document defines the interface contracts for the console-based todo application. Since this is a console application, the contracts specify the interactions between the user and the system through the command-line interface.

## Core Task Management Interface

### 1. Add Task Interface
**Operation**: Add a new task to the todo list

**Input Parameters**:
- `title` (String, Required): The title of the task
- `description` (String, Optional): Detailed description of the task

**User Interaction Flow**:
1. User selects "Add Task" from main menu
2. System prompts for task title
3. System prompts for optional description
4. System validates input and creates task
5. System confirms task creation with unique ID

**Output**:
- Success: Confirmation message with task ID and details
- Error: Appropriate error message for invalid input

**Validation Rules**:
- Title must not be empty or only whitespace
- Title and description should have reasonable length limits for console display

### 2. View All Tasks Interface
**Operation**: Display all tasks with their status

**Input Parameters**: None

**User Interaction Flow**:
1. User selects "View All Tasks" from main menu
2. System retrieves all tasks
3. System displays each task with ID, title, description, and completion status

**Output**:
- Success: List of all tasks with visual indicators for completion status
- Error: "No tasks found" message if no tasks exist

### 3. Update Task Interface
**Operation**: Modify an existing task's title or description

**Input Parameters**:
- `task_id` (Integer, Required): The ID of the task to update
- `title` (String, Optional): New title for the task
- `description` (String, Optional): New description for the task

**User Interaction Flow**:
1. User selects "Update Task" from main menu
2. System displays all tasks for reference
3. System prompts for task ID to update
4. System prompts for new title (or skip to keep current)
5. System prompts for new description (or skip to keep current)
6. System validates input and updates task

**Output**:
- Success: Confirmation message of successful update
- Error: Appropriate error message for invalid task ID or input

### 4. Delete Task Interface
**Operation**: Remove a task from the todo list

**Input Parameters**:
- `task_id` (Integer, Required): The ID of the task to delete

**User Interaction Flow**:
1. User selects "Delete Task" from main menu
2. System displays all tasks for reference
3. System prompts for task ID to delete
4. System confirms deletion with user
5. System validates input and deletes task

**Output**:
- Success: Confirmation message of successful deletion
- Error: Appropriate error message for invalid task ID

**Validation Rules**:
- User must confirm deletion before operation proceeds
- Task must exist before deletion can occur

### 5. Mark Task Complete Interface
**Operation**: Update a task's status to complete

**Input Parameters**:
- `task_id` (Integer, Required): The ID of the task to mark complete

**User Interaction Flow**:
1. User selects "Mark Task Complete" from main menu
2. System displays all tasks for reference
3. System prompts for task ID to mark complete
4. System validates input and updates task status

**Output**:
- Success: Confirmation message of successful status update
- Error: Appropriate error message for invalid task ID

### 6. Mark Task Incomplete Interface
**Operation**: Update a task's status to incomplete

**Input Parameters**:
- `task_id` (Integer, Required): The ID of the task to mark incomplete

**User Interaction Flow**:
1. User selects "Mark Task Incomplete" from main menu
2. System displays all tasks for reference
3. System prompts for task ID to mark incomplete
4. System validates input and updates task status

**Output**:
- Success: Confirmation message of successful status update
- Error: Appropriate error message for invalid task ID

## Main Menu Interface

### Menu Options
The application provides the following main menu options:

1. **Add Task** - Add a new task to the list
2. **View All Tasks** - Display all tasks with status indicators
3. **Update Task** - Modify an existing task's details
4. **Delete Task** - Remove a task from the list
5. **Mark Task as Complete** - Update task status to complete
6. **Mark Task as Incomplete** - Update task status to incomplete
7. **Exit** - Quit the application

### User Input Validation
All user inputs are validated according to these rules:
- Menu choices must be numeric values between 1 and 7
- Task IDs must be numeric values that correspond to existing tasks
- Text inputs (titles, descriptions) must meet validation criteria
- Invalid inputs result in appropriate error messages and re-prompting

## Internal API Contracts

### TodoApp Class Interface
The CLI interface interacts with the TodoApp class through these methods:

- `add_task(title, description)` - Returns created Task object
- `get_all_tasks()` - Returns list of all Task objects
- `get_task_by_id(task_id)` - Returns specific Task object or None
- `update_task(task_id, title, description)` - Returns boolean success indicator
- `delete_task(task_id)` - Returns boolean success indicator
- `mark_task_complete(task_id)` - Returns boolean success indicator
- `mark_task_incomplete(task_id)` - Returns boolean success indicator

### Error Handling Contracts
All operations follow these error handling patterns:
- Invalid inputs result in user-friendly error messages
- Non-existent tasks result in appropriate notifications
- System errors are handled gracefully with fallback behaviors
- User is prompted to retry operations when possible