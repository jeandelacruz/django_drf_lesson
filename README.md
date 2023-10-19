# Django Sesion

## Comandos

[Link](DJANGO.md)

## Apps

- Author, puede tener varios **Books** (Relación de uno a muchos)
- Book, puede pertenecer a diferentes **Genres**; Genre, puede tener varios **Books** (Relación de muchos a muchos)
- Profile, pertenece a un solo **Author** (Relacion de uno a uno)

#### Authors

| columna | tipo         |
| ------- | ------------ |
| id      | int PK Auto  |
| name    | varchar(100) |

#### Books

| columna   | tipo                |
| --------- | ------------------- |
| id        | int PK Auto         |
| title     | varchar(100)        |
| author_id | int FK (authors.id) |

#### Genrs

| columna | tipo         |
| ------- | ------------ |
| id      | int PK Auto  |
| name    | varchar(100) |

#### BooksGenrs (Pivote)

| columna  | tipo              |
| -------- | ----------------- |
| id       | int PK Auto       |
| genre_id | int FK (genrs.id) |
| book_id  | int FK (books.id) |

#### Profiles

| columna   | tipo                |
| --------- | ------------------- |
| id        | int PK Auto         |
| bio       | text                |
| author_id | int FK (authors.id) |
