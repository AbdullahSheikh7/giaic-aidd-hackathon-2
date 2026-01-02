# Data Model: Web Todo App

## Overview
This document defines the data model for the web-based todo application, detailing the structure of entities and their relationships in the Neon Serverless PostgreSQL database using Prisma ORM.

## Entity: User

### Schema Definition (Prisma)
```prisma
model User {
  id           String   @id @default(cuid())
  email        String   @unique
  name         String?
  password     String   // hashed password
  createdAt    DateTime @default(now())
  updatedAt    DateTime @updatedAt

  // Relations
  tasks        Task[]

  @@map("users")
}
```

### Attributes
- **id** (String)
  - Description: Unique identifier for each user
  - Constraints: Auto-generated using cuid(), unique, non-null
  - Type: String (Prisma cuid() function)

- **email** (String)
  - Description: User's email address used for authentication
  - Constraints: Unique, non-null, valid email format
  - Validation: Must be a properly formatted email address

- **name** (String, optional)
  - Description: User's display name
  - Constraints: Optional, nullable
  - Validation: Can be null or empty

- **password** (String)
  - Description: Hashed password for authentication
  - Constraints: Non-null, securely hashed
  - Security: Never stored in plain text, always hashed

- **createdAt** (DateTime)
  - Description: Timestamp when the user account was created
  - Constraints: Auto-generated, non-null
  - Format: ISO 8601 format

- **updatedAt** (DateTime)
  - Description: Timestamp when the user account was last updated
  - Constraints: Auto-updated, non-null
  - Format: ISO 8601 format, automatically updated on changes

## Entity: Task

### Schema Definition (Prisma)
```prisma
model Task {
  id          String   @id @default(cuid())
  title       String
  description String?
  completed   Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  // Relations
  userId      String
  user        User     @relation(fields: [userId], references: [id])

  @@map("tasks")
}
```

### Attributes
- **id** (String)
  - Description: Unique identifier for each task
  - Constraints: Auto-generated using cuid(), unique, non-null
  - Type: String (Prisma cuid() function)

- **title** (String)
  - Description: The main title or subject of the task
  - Constraints: Required, non-null, max length reasonable for UI display
  - Validation: Must not be empty or only whitespace

- **description** (String)
  - Description: Optional detailed information about the task
  - Constraints: Optional, nullable, max length reasonable for UI display
  - Validation: Can be empty or null

- **completed** (Boolean)
  - Description: Status indicator showing whether the task is completed
  - Constraints: Required, non-null, default value false
  - Values: true (completed) or false (incomplete)

- **createdAt** (DateTime)
  - Description: Timestamp when the task was created
  - Constraints: Auto-generated, non-null
  - Format: ISO 8601 format

- **updatedAt** (DateTime)
  - Description: Timestamp when the task was last modified
  - Constraints: Auto-updated, non-null
  - Format: ISO 8601 format, automatically updated on changes

- **userId** (String)
  - Description: Foreign key linking the task to its owner user
  - Constraints: Required, non-null, references User.id
  - Relationship: Each task belongs to exactly one user

## Relationships

### User → Task (One-to-Many)
- One user can own many tasks
- Each task belongs to exactly one user
- Foreign key: Task.userId references User.id
- Cascade behavior: Tasks are deleted when user is deleted

## Validation Rules

### User Validation
1. **Email Uniqueness**: Each email address must be unique across all users
2. **Email Format**: Email must be a valid email format
3. **Password Security**: Password must be properly hashed before storage

### Task Validation
1. **Title Required**: Task title must be provided and not empty
2. **User Ownership**: Each task must belong to a valid user
3. **ID Uniqueness**: Each task must have a unique ID within the system
4. **Status Integrity**: Completed status can only be true or false

## Database Indexes
- User.email: Unique index for fast authentication lookups
- Task.userId: Index for efficient retrieval of user-specific tasks
- Task.createdAt: Index for sorting tasks by creation date

## State Transitions
- **Task Creation**: When created, task has `completed = false` and current timestamps
- **Complete Transition**: Task moves from `completed = false` to `completed = true`
- **Incomplete Transition**: Task moves from `completed = true` to `completed = false`
- **Update Transition**: Any field except ID and userId can be updated, triggering `updatedAt` update

## Security Considerations
- All tasks are associated with a specific user via userId foreign key
- API endpoints must verify that users can only access tasks belonging to them
- Proper authentication and authorization checks required for all operations
- User passwords must be securely hashed using industry-standard algorithms