<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.0.0 (initial version)
- List of modified principles:
  - PRINCIPLE_1_NAME → Python-First Development
  - PRINCIPLE_2_NAME → CLI Interface Standard
  - PRINCIPLE_3_NAME → Test-First (NON-NEGOTIABLE)
  - PRINCIPLE_4_NAME → In-Memory Storage Pattern
  - PRINCIPLE_5_NAME → UV Package Management
- Added sections: Development Standards, Quality Assurance
- Removed sections: None
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - README.md ⚠ pending
- Follow-up TODOs: None
-->

# Todo App Constitution

## Core Principles

### Python-First Development
All features and functionality must be implemented using Python 3.13+ as the primary language. Code must follow Python best practices, maintain clean architecture with separation of concerns between models, services, and interfaces. All new features must be implemented as extensions to existing Python classes and modules following the established patterns in src/todo_app.py.

### CLI Interface Standard
Every core functionality must be accessible through the command-line interface. The CLI must follow standard input/output patterns with clear user prompts, proper error handling, and consistent formatting. All user interactions must be intuitive and follow the menu-driven approach established in src/main.py with appropriate validation and feedback.

### Test-First (NON-NEGOTIABLE)
All new features must have corresponding tests written before implementation. Tests must be added to test_todo.py following the established pattern of independent functionality verification. The red-green-refactor cycle must be followed with all tests passing before code is considered complete. Test coverage must include all basic functionality: Add Task, Delete Task, Update Task, View Task List, and Mark as Complete.

### In-Memory Storage Pattern
All data persistence must follow the in-memory storage pattern established in the TodoApp class. No external databases or persistent storage files should be introduced without explicit architectural approval. The application state must remain consistent with the existing Task model and TodoApp collection management approach.

### UV Package Management
All dependencies must be managed using UV package manager as specified in pyproject.toml. No other package managers (pip, conda) should be used for dependency management. All development and runtime dependencies must be explicitly declared in pyproject.toml with appropriate version constraints.

## Development Standards

### Code Quality Requirements
- All code must follow Python PEP 8 style guidelines
- Type hints must be used for all function parameters and return values
- Comprehensive docstrings required for all classes and methods
- Error handling must be implemented consistently throughout the codebase
- No hardcoded values - use constants where appropriate

### Architecture Constraints
- Maintain separation between models (Task class) and business logic (TodoApp class)
- CLI interface must remain separate from core application logic
- Follow existing patterns for method naming and class structure
- Preserve backward compatibility for existing functionality
- All new features must integrate seamlessly with existing menu system

## Quality Assurance

### Code Review Process
- All pull requests must include updated tests for new functionality
- Code must pass all existing tests before merging
- Changes must maintain the existing user experience unless explicitly specified
- Performance impact must be considered for all changes
- Security implications must be evaluated for any new input/output operations

### Testing Requirements
- All basic functionality tests must pass (Add, Delete, Update, View, Complete)
- New features must include both positive and negative test cases
- Error conditions must be tested and handled appropriately
- Integration between components must be verified
- User input validation must be thoroughly tested

## Governance

All development must comply with this constitution. Amendments require documentation of the change, justification for deviation from existing principles, and approval from project maintainers. All pull requests must verify compliance with these principles before merging. The constitution supersedes any conflicting practices or patterns established in the codebase.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
