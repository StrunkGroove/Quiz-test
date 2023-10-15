# Quiz-test
Bewise-test

### For start:
```
nano .env  
```
```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
POSTGRES_PORT=5432
POSTGRES_HOST=postgres

PGADMIN_DEFAULT_EMAIL=user@mail.ru
PGADMIN_DEFAULT_PASSWORD=password
```


### Build and run the Docker containers
```
docker-compose build
docker-compose up
```


### Enter Docker shell for migration
```
docker exec -it quiz-test-web-1 bash
```
```
alembic revision --autogenerate -m 'initial'
alembic upgrade head
```

### Go to and test!
```
0.0.0.0:8080/docs
```
