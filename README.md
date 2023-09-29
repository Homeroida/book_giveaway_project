# Book Giveaway API

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Libraries Used](#Libraries-Used)
5. [Installation and Setup](#installation-and-setup)
6. [Docker Setup](#docker-setup)
7. [API Endpoints](#api-endpoints)
8. [Business Logic](#business-logic)
9. [Swagger Documentation](#swagger-documentation)
10. [Contributing](#contributing)

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

### Docker

- Platform for containerizing.

## Libraries Used

### Django REST Framework

- Toolkit for building Web APIs on top of Django.

### django-filter

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

6. **Create SuperUser**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## Docker Setup

### Overview

This section provides guidelines for building and running the Book Giveaway API project using Docker. Docker helps you to containerize the application, ensuring that it runs the same regardless of where it's deployed.

### Prerequisites

- Docker installed on your machine. [Get Docker](https://docs.docker.com/get-docker/)
- Docker Compose installed if you're using Windows or macOS. [Get Docker Compose](https://docs.docker.com/compose/install/)

### Steps

#### 1. Build Docker Image

Navigate to the project directory where the `Dockerfile` is located and run the following command to build the Docker image.

```bash
docker build -t book_giveaway_api .
```

This will build the Docker image with the name `book_giveaway_api`.

#### 2. Run Docker Container

To run the Docker container, execute the following command:

```bash
docker run -p 8000:8000 book_giveaway_api
```

This will map port 8000 inside the container to port 8000 on your host machine.

#### 3. Check API

Open your browser and navigate to `http://localhost:8000` to confirm that the API is running.

#### 4. Stop Docker Container

To stop the running container, you can use the `docker stop` command with the container ID or name.

```bash
docker stop [CONTAINER_ID_OR_NAME]
```

### Docker Compose (Optional)

If you're using Docker Compose, you can define services in a `docker-compose.yml` file. To bring up the services, use:

```bash
docker-compose up
```

To stop them:

```bash
docker-compose down
```

### Troubleshooting

If you encounter any issues while setting up or running the Docker container, consult the [Docker documentation](https://docs.docker.com/get-started/overview/) for troubleshooting tips.

## API Endpoints

- `/register/`: User Registration
- `/login/`: User Login
- `/books/`: CRUD operations for books
- `/authors/`: CRUD operations for authors
- `/genres/`: CRUD operations for genres
- `/conditions/`: CRUD operations for conditions
- `/photos/`: CRUD operations for photos

## Swagger Documentation

- Access the Swagger documentation at `/docs/`
- Access the redoc documentation at `/redoc/`

## Business Logic

The core logic of the application revolves around the management of books and users. The API provides a set of functionalities for users to add, edit, delete, or give away books. The book listing and retrieval are optimized through the use of pagination, ensuring a smooth user experience even with a large dataset.

## Contributing

Feel free to fork the project, open a PR, or submit an issue.
