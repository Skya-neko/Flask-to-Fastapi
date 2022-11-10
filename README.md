
# Build Environment
## PostgreSQL setting
### create table
![](img/DDL_createTable.png)
### see table schema
![](img/personTableSchema.png)
### insert data
![](img/InsertInto.png)


## Docker command
Use following command in ./fastapi

Build

```docker build -t fastapi .```

Run

```docekr run -p 8080:8080 fastapi```

# Project result

## API docs
connect to `http://127.0.0.1:8080/docs` and see API docs.

## Response
