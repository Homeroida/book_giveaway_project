# Book Giveaway API

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Libraries Used](#Libraries-Used)
5. [Installation and Setup](#installation-and-setup)
6. [API Endpoints](#api-endpoints)
7. [Business Logic](#business-logic)
8. [Swagger Documentation](#swagger-documentation)
9. [Contributing](#contributing)

## Overview

This is a Django RESTful API project for a book giveaway platform. The API allows users to manage books they want to give away, filter books based on various parameters, and manage supporting resources like authors and genres. It also includes user authentication and a feature for book owners to select a recipient if multiple people are interested in a book.

## Features

### User Authentication

- **Registration with Email**: Users can register using their email address. The registration endpoint is `/register/`.
- **Login**: Users can log in using their email and password. The login endpoint is `/login/`.

### Books Management

- **CRUD Operations**: Users can create, read, update, and delete books. The CRUD operations are handled by the `BookViewSet` class.
- **Book Filtering**: Users can filter books based on various parameters like author, genre, etc., using the `BookFilter` class.

### Supporting Resources

- **Authors, Genres, and Conditions**: The API allows users to manage authors, genres, and conditions. These are managed by the `AuthorViewSet`, `GenreViewSet`, and `ConditionViewSet` classes respectively.

### Book Retrieval Information

- **Location**: Each book has a `location` field that indicates where the book can be picked up.

### Ownership Decision

- **Recipient Selection**: If multiple people are interested in a book, the owner has the capability to choose the recipient. This is managed by the `InterestViewSet` class and the `select_recipient` method.

## Technologies Used

### Django

- Web framework for building the API.

### SQLite

- Database used for development.

## Libraries Used

### Django REST Framework

- Toolkit for building Web APIs on top of Django.

## django-filter

### How to Use Filters

The API uses the `django-filter` library for creating complex queries for filtering books. You can use the filters by appending query parameters to the API endpoint for books.

### Examples:

1. **Filter by Author:** To get books by a particular author, you can use the `author` query parameter.

   ```
   GET /books/?author=author
   ```

2. **Filter by Genre:** To get books of a specific genre, use the `genre` query parameter.
   ```
   GET /books/?genre=genre
   ```

You can combine multiple filters as well:

```
GET /books/?author=author&genre=genre
```

### Pagination

- Pagination is implemented using Django REST Framework's built-in pagination classes.

### drf-spectacular

- Used for generating the Swagger documentation for the API.

### Pillow

- Used for handling image uploads for book covers.

## Installation and Setup

### Setting Up a Virtual Environment

Before you begin, it's advisable to set up a Python virtual environment. This isolates your project and avoids conflicts with other packages. Here's how to create one:

#### For macOS and Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:

```bash
python3 -m venv venv
source venv/bin/activate
```

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Homeroida/book_giveaway_project.git
   ```

2. **Navigate to Project Directory**

   ```bash
   cd book_giveaway_project
   ```

3. **Activate the Virtual Environment**

#### For macOS and Linux:

```bash
source venv/bin/activate
```

#### For Windows:

```bash
venv\Scripts\activate
```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `/register/`: User Registration
- `/login/`: User Login
- `/books/`: CRUD operations for books
- `/authors/`: CRUD operations for authors
- `/genres/`: CRUD operations for genres
- `/conditions/`: CRUD operations for conditions

## Swagger Documentation

- Access the Swagger documentation at `/docs/`
- Access the redoc documentation at `/redoc/`

## Business Logic

The core logic of the application revolves around the management of books and users. The API provides a set of functionalities for users to add, edit, delete, or give away books. The book listing and retrieval are optimized through the use of pagination, ensuring a smooth user experience even with a large dataset.

## Contributing

Feel free to fork the project, open a PR, or submit an issue.
