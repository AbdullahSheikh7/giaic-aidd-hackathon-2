# Data Model: Console Todo App

## Overview
This document defines the data model for the console-based todo application, detailing the structure of tasks and their relationships.

## Entity: Task

### Attributes
- **id** (Integer)
  - Description: Unique identifier for each task
  - Constraints: Auto-incrementing, non-null, unique
  - Generated: Automatically assigned when task is created

- **title** (String)
  - Description: The main title or subject of the task
  - Constraints: Required, non-null, max length reasonable for console display
  - Validation: Must not be empty or only whitespace

- **description** (String)
  - Description: Optional detailed information about the task
  - Constraints: Optional, nullable, max length reasonable for console display
  - Validation: Can be empty or null

- **completed** (Boolean)
  - Description: Status indicator showing whether the task is completed
  - Constraints: Required, non-null, default value false
  - Values: true (completed) or false (incomplete)

- **created_at** (DateTime)
  - Description: Timestamp when the task was created
  - Constraints: Required, non-null, auto-generated
  - Format: ISO 8601 format for consistent serialization

- **updated_at** (DateTime)
  - Description: Timestamp when the task was last modified
  - Constraints: Required, non-null, auto-updated
  - Format: ISO 8601 format for consistent serialization
  - Behavior: Updated whenever any task property changes

### State Transitions
- **Initial State**: When created, task has `completed = false`
- **Complete Transition**: Task moves from `completed = false` to `completed = true`
- **Incomplete Transition**: Task moves from `completed = true` to `completed = false`
- **Update Transition**: Any field except ID can be updated, triggering `updated_at` update

### Validation Rules
1. **Title Required**: Task title must be provided and not empty
2. **ID Uniqueness**: Each task must have a unique ID within the system
3. **Status Integrity**: Completed status can only be true or false
4. **Timestamp Consistency**: created_at should always be before or equal to updated_at

### Data Relationships
- The Task entity exists independently within the system
- No external relationships to other entities in the current scope
- All tasks are managed within a single TodoApp instance

## Collection: TodoApp

### Attributes
- **tasks** (List of Task objects)
  - Description: Collection of all tasks in the system
  - Constraints: Maintains all Task objects in memory

- **next_id** (Integer)
  - Description: The next available ID to assign to a new task
  - Constraints: Automatically incremented after each new task

### Operations
- **Add Task**: Creates a new Task and adds it to the collection
- **Get All Tasks**: Returns all tasks in the collection
- **Get Task by ID**: Returns a specific task by its ID
- **Update Task**: Modifies an existing task's properties
- **Delete Task**: Removes a task from the collection
- **Mark Complete**: Updates the completed status of a task to true
- **Mark Incomplete**: Updates the completed status of a task to false