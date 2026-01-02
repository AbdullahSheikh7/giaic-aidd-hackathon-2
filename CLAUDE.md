# Claude Code Instructions for Todo App

This document provides instructions for using Claude Code to work with the Todo App project.

## Project Overview

The Todo App is a command-line application that allows users to manage tasks with in-memory storage. It implements all 5 Basic Level features:
1. Add Task
2. Delete Task
3. Update Task
4. View Task List
5. Mark as Complete

## Project Structure

```
├── src/
│   ├── todo_app.py     # Main todo application class with Task model
│   └── main.py         # CLI interface
├── test_todo.py        # Test file for functionality verification
├── pyproject.toml      # Project configuration with dependencies
├── README.md           # Setup and usage instructions
├── CLAUDE.md           # This file
└── PHASE_1.md          # Phase 1 requirements
```

## Working with the Code

### Key Classes

- `Task` class in `src/todo_app.py`: Represents a single todo task with id, title, description, and completion status
- `TodoApp` class in `src/todo_app.py`: Main application class that manages the collection of tasks
- CLI interface in `src/main.py`: Command-line interface for user interaction

### Adding Features

To add new features to the todo application:

1. First consider if the feature belongs to the Intermediate or Advanced Level
2. Update the `TodoApp` class with new methods if needed
3. Add corresponding interface functions in `main.py`
4. Update the menu and choice handling to include the new functionality

### Testing

Run the test file to verify all basic functionality:
```bash
python test_todo.py
```

### Running the Application

```bash
uv run python src/main.py
```

## Extending the Application

The application is designed with extensibility in mind. Future enhancements could include:

- Adding priority levels and categories (Intermediate Level)
- Implementing search and filter capabilities (Intermediate Level)
- Adding due dates and time reminders (Advanced Level)
- Creating recurring tasks functionality (Advanced Level)

## UV Package Management

This project uses UV for package management:
- To sync dependencies: `uv sync`
- To run the application: `uv run python src/main.py`
- To install in development mode: `uv pip install -e .`

## Development Workflow

When using Claude Code for this project:
1. Use the existing architecture patterns for consistency
2. Follow the same coding style and naming conventions
3. Update the test file when adding new functionality
4. Ensure all basic functionality remains intact when adding features

## Active Technologies
- Python 3.13+ (as specified in project constitution and pyproject.toml) + None required beyond standard library (as per existing architecture) (001-console-todo-app)
- In-memory storage using existing TodoApp class structure (as per constitution) (001-console-todo-app)
- Python 3.13+ (for FastAPI backend), JavaScript/TypeScript (for Next.js frontend) + FastAPI (backend framework), Next.js (frontend framework), Prisma (ORM), Better Auth (authentication), Neon PostgresSQL (database) (002-web-todo-app)
- Neon Serverless PostgreSQL database with Prisma ORM for data access (002-web-todo-app)

## Recent Changes
- 001-console-todo-app: Added Python 3.13+ (as specified in project constitution and pyproject.toml) + None required beyond standard library (as per existing architecture)
