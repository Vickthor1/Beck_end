# PostgreSQL with Alembic Migrations

This project sets up a PostgreSQL database using Docker and manages schema migrations with Alembic.

## Setup

1. Ensure Docker is installed and running.

2. Start the PostgreSQL container:
   ```
   docker-compose up -d
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations to create the database and tables:
   ```
   alembic upgrade head
   ```

## Models

- User: id (int), name (str), email (str)

## Hosting on GitHub

1. Initialize Git repository:
   ```
   git init
   ```

2. Add files:
   ```
   git add .
   ```

3. Commit:
   ```
   git commit -m "Initial commit"
   ```

4. Create a repository on GitHub.

5. Add remote:
   ```
   git remote add origin https://github.com/yourusername/yourrepo.git
   ```

6. Push:
   ```
   git push -u origin main
   ```