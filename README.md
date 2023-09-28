# Book Giveaway API

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation and Setup](#installation-and-setup)
5. [API Endpoints](#api-endpoints)
6. [Swagger Documentation](#swagger-documentation)
7. [Contributing](#contributing)

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


## Libraries Used

### Django
- Web framework for building the API.

### Django REST Framework
- Toolkit for building Web APIs on top of Django.

### django-filter
- Used for creating complex queries for filtering books.

### drf-spectacular
- Used for generating the Swagger documentation for the API.

### Pillow
- Used for handling image uploads for book covers.

### SQLite
- Database used for development.

## Installation and Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Homeroida/book_giveaway_project.git
    ```

2. **Navigate to Project Directory**
    ```bash
    cd book_giveaway_project
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Server**
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
- Access the Swagger documentation at `/schema/docs/`

## Contributing

Feel free to fork the project, open a PR, or submit an issue.
