# API Contracts: Web Todo App

## Overview
This document defines the API contracts for the web-based todo application. All endpoints follow RESTful conventions and require user authentication.

## Authentication
All API endpoints require authentication using Better Auth tokens. The token must be provided in the Authorization header as a Bearer token.

```
Authorization: Bearer {token}
```

## API Endpoints

### 1. List All Tasks
**Endpoint**: `GET /api/{user_id}/tasks`

**Description**: Retrieve all tasks for a specific user

**Path Parameters**:
- `user_id` (String): The ID of the user whose tasks to retrieve

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Query Parameters**:
- `completed` (Boolean, optional): Filter tasks by completion status
- `limit` (Integer, optional): Maximum number of tasks to return (default: 50)
- `offset` (Integer, optional): Number of tasks to skip (for pagination)

**Response**:
- **Success (200 OK)**:
  ```json
  {
    "tasks": [
      {
        "id": "task_id_1",
        "title": "Task title",
        "description": "Task description",
        "completed": false,
        "createdAt": "2026-01-03T10:00:00Z",
        "updatedAt": "2026-01-03T10:00:00Z",
        "userId": "user_id"
      }
    ],
    "total": 1,
    "limit": 50,
    "offset": 0
  }
  ```

- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to access these tasks
- **Not Found (404)**: User ID does not exist

### 2. Create a New Task
**Endpoint**: `POST /api/{user_id}/tasks`

**Description**: Create a new task for a specific user

**Path Parameters**:
- `user_id` (String): The ID of the user for whom to create the task

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Request Body**:
```json
{
  "title": "Task title",
  "description": "Task description (optional)"
}
```

**Response**:
- **Success (201 Created)**:
  ```json
  {
    "id": "new_task_id",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "createdAt": "2026-01-03T10:00:00Z",
    "updatedAt": "2026-01-03T10:00:00Z",
    "userId": "user_id"
  }
  ```

- **Bad Request (400)**: Invalid request body (e.g., missing title, invalid format)
- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to create tasks for this user ID
- **Not Found (404)**: User ID does not exist

### 3. Get Task Details
**Endpoint**: `GET /api/{user_id}/tasks/{id}`

**Description**: Retrieve details of a specific task

**Path Parameters**:
- `user_id` (String): The ID of the user who owns the task
- `id` (String): The ID of the task to retrieve

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Response**:
- **Success (200 OK)**:
  ```json
  {
    "id": "task_id",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "createdAt": "2026-01-03T10:00:00Z",
    "updatedAt": "2026-01-03T10:00:00Z",
    "userId": "user_id"
  }
  ```

- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to access this task
- **Not Found (404)**: Task ID or User ID does not exist

### 4. Update a Task
**Endpoint**: `PUT /api/{user_id}/tasks/{id}`

**Description**: Update details of a specific task

**Path Parameters**:
- `user_id` (String): The ID of the user who owns the task
- `id` (String): The ID of the task to update

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated task description"
}
```

**Response**:
- **Success (200 OK)**:
  ```json
  {
    "id": "task_id",
    "title": "Updated task title",
    "description": "Updated task description",
    "completed": false,
    "createdAt": "2026-01-03T10:00:00Z",
    "updatedAt": "2026-01-03T11:00:00Z",
    "userId": "user_id"
  }
  ```

- **Bad Request (400)**: Invalid request body
- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to update this task
- **Not Found (404)**: Task ID or User ID does not exist

### 5. Delete a Task
**Endpoint**: `DELETE /api/{user_id}/tasks/{id}`

**Description**: Delete a specific task

**Path Parameters**:
- `user_id` (String): The ID of the user who owns the task
- `id` (String): The ID of the task to delete

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Response**:
- **Success (200 OK)**:
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```

- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to delete this task
- **Not Found (404)**: Task ID or User ID does not exist

### 6. Toggle Task Completion Status
**Endpoint**: `PATCH /api/{user_id}/tasks/{id}/complete`

**Description**: Toggle the completion status of a specific task

**Path Parameters**:
- `user_id` (String): The ID of the user who owns the task
- `id` (String): The ID of the task to update

**Request Headers**:
- `Authorization`: Bearer token for authentication

**Request Body**:
```json
{
  "completed": true
}
```

**Response**:
- **Success (200 OK)**:
  ```json
  {
    "id": "task_id",
    "title": "Task title",
    "description": "Task description",
    "completed": true,
    "createdAt": "2026-01-03T10:00:00Z",
    "updatedAt": "2026-01-03T11:00:00Z",
    "userId": "user_id"
  }
  ```

- **Bad Request (400)**: Invalid request body (e.g., missing completed field)
- **Unauthorized (401)**: Invalid or missing authentication token
- **Forbidden (403)**: User does not have permission to update this task
- **Not Found (404)**: Task ID or User ID does not exist

## Common Error Responses

### 400 Bad Request
```json
{
  "error": "Bad Request",
  "message": "Detailed error message explaining the issue",
  "details": {
    "field": "value causing the error"
  }
}
```

### 401 Unauthorized
```json
{
  "error": "Unauthorized",
  "message": "Authentication token is invalid or missing"
}
```

### 403 Forbidden
```json
{
  "error": "Forbidden",
  "message": "User does not have permission to access this resource"
}
```

### 404 Not Found
```json
{
  "error": "Not Found",
  "message": "The requested resource was not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal Server Error",
  "message": "An unexpected error occurred"
}
```

## Data Validation Rules

### Task Title
- Required: Yes
- Type: String
- Minimum Length: 1 character
- Maximum Length: 255 characters
- Must not be only whitespace

### Task Description
- Required: No (optional)
- Type: String
- Maximum Length: 1000 characters

### Completed Status
- Required: Yes for PATCH requests
- Type: Boolean
- Values: true or false