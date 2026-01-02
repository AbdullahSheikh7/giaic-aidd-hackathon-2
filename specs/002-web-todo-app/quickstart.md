# Quickstart Guide: Web Todo App

## Overview
This guide provides instructions for quickly getting started with the web-based todo application. The app is built with a Next.js frontend and FastAPI backend, using Neon Serverless PostgreSQL for data storage and Better Auth for authentication.

## Prerequisites
- Node.js 18+ installed on your system
- Python 3.13+ installed on your system
- npm or pnpm package manager
- UV package manager for Python dependencies
- Git for version control

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Set up the Backend Server
1. Navigate to the server directory:
```bash
cd server
```

2. Install Python dependencies using UV:
```bash
uv sync
```

3. Set up environment variables:
```bash
cp .env.example .env
```
Then edit the .env file with your configuration:
- `DATABASE_URL`: Neon Serverless PostgreSQL connection string
- `AUTH_SECRET`: Secret key for authentication
- `NEXT_PUBLIC_APP_URL`: URL of your deployed application
```

4. Initialize the database with Prisma:
```bash
cd ../prisma
npx prisma migrate dev --name init
```

5. Start the backend server:
```bash
cd ../server
uv run python src/main.py
```

### 3. Set up the Frontend Client
1. Navigate to the client directory:
```bash
cd client
```

2. Install JavaScript dependencies:
```bash
npm install
# or
pnpm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
```
Then edit the .env.local file with your configuration:
- `NEXT_PUBLIC_API_URL`: URL of your backend API (e.g., http://localhost:8000)
- `NEXT_PUBLIC_APP_URL`: URL of your frontend application
```

4. Start the frontend development server:
```bash
npm run dev
# or
pnpm dev
```

## First Steps

### 1. Access the Application
Open your browser and navigate to:
```
http://localhost:3000
```

### 2. Create an Account
1. Click on the "Sign Up" button
2. Enter your email and password
3. Complete the verification process if required
4. You'll be redirected to the dashboard

### 3. Add Your First Task
1. On the dashboard, click the "Add Task" button or form
2. Enter a title for your task (required)
3. Optionally add a description
4. Click "Create Task"
5. Your task will appear in the task list

## Common Operations

### Viewing Tasks
- All tasks for the authenticated user are displayed on the main dashboard
- Use the filter options to show all, completed, or pending tasks
- Tasks are sorted by creation date by default

### Updating a Task
1. Click the edit button on the task you want to update
2. Modify the title or description
3. Click "Save" to update the task

### Marking Tasks Complete/Incomplete
1. Click the checkbox next to a task to toggle its completion status
2. The task will be visually updated to reflect the new status
3. The change is saved automatically to the backend

### Deleting a Task
1. Click the delete button (trash icon) on the task you want to remove
2. Confirm the deletion when prompted
3. The task will be removed from the list and database

## API Endpoints

The application uses the following API structure:

### Task Management
- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a specific task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion status

### Authentication
- `/api/auth/*` - Better Auth endpoints for signup, signin, etc.

## Development Commands

### Backend (Server)
```bash
# Install dependencies
uv sync

# Run the development server
uv run python src/main.py

# Run tests
uv run pytest

# Format code
uv run black .
uv run ruff check --fix
```

### Frontend (Client)
```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Run tests
npm run test

# Format code
npm run format
npm run lint
```

### Database (Prisma)
```bash
# Generate Prisma client
npx prisma generate

# Run migrations
npx prisma db push

# Open Prisma Studio (database GUI)
npx prisma studio
```

## Troubleshooting

### Common Issues
- **Port already in use**: Change the port in `server/src/main.py` or `client/next.config.js`
- **Database connection errors**: Verify your Neon PostgreSQL connection string in the .env file
- **Authentication not working**: Check that the AUTH_SECRET is properly set and consistent between client and server
- **API calls failing**: Verify that NEXT_PUBLIC_API_URL points to your running backend server

### Error Messages
- "Unauthorized": Your authentication token may have expired; try signing in again
- "Forbidden": You may be trying to access resources that don't belong to you
- "Database connection failed": Check your database configuration and connection string
- "Validation error": Check that your request body matches the expected schema

## Next Steps
- Explore the API documentation at `/docs` and `/redoc` endpoints on the backend
- Review the Prisma schema in the `prisma/` directory to understand the data model
- Check the Next.js pages in `client/src/pages` to understand the frontend routing
- Review the FastAPI routes in `server/src/routes` to understand the backend implementation
- Set up proper environment variables for production deployment