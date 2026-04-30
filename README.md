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

---

# PostgreSQL com Migrações Alembic

Este projeto configura um banco de dados PostgreSQL usando Docker e gerencia migrações de esquema com Alembic.

## Configuração

1. Certifique-se de que o Docker está instalado e em execução.

2. Inicie o contêiner PostgreSQL:
   ```
   docker-compose up -d
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute as migrações para criar o banco de dados e as tabelas:
   ```
   alembic upgrade head
   ```

## Modelos

- Usuário: id (int), nome (str), email (str)

## Hospedagem no GitHub

1. Inicialize o repositório Git:
   ```
   git init
   ```

2. Adicione os arquivos:
   ```
   git add .
   ```

3. Faça commit:
   ```
   git commit -m "Commit inicial"
   ```

4. Crie um repositório no GitHub.

5. Adicione o remoto:
   ```
   git remote add origin https://github.com/seuusuario/seurepo.git
   ```

6. Push:
   ```
   git push -u origin main
   ```