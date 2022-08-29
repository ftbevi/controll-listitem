# Management Invetiment

Challenge project for backend developer.

## Build Instructions

1. create .env file using .env-example file.
```

SECRET_KEY=secret_key
ALLOWED_HOSTS=*
DEBUG=True

DATABASE_URL=postgres://controllitem:controllitem@db:5432/controllitem

```

2. Run command for install e configure development environment.

```bash
make setup
```

3. Run command for execute project. open in you browser http://localhost:6600/ and go direct in admin.

```bash
make run
```

4. make login using credentials created in make setup command.

```
user: dev
password: controllitem@#2022
```

When your avaliation is finish, then run command for kill all container.

## Interesting Commands

When your avaliation is finish, then run command for kill all container.

```bash
make stop
```

Command for update database executing makemigrations and migrate.

```bash
make dbupdate
```

Command for execute just makemigrations.

```bash
make makemigrations
```

Command for execute just migrate.

```bash
make migrate
```

Command for clean dev environment fully.

```bash
make clean
```

### Third-party Libraries
- djangorestframework
- django extensions
- dj-database-url 
- python-decouple 
- django
