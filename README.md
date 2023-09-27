# Book Giveaway API

## Overview

This is a Django RESTful API project for a book giveaway platform. The API allows users to manage books they want to give away, filter books based on various parameters, and manage supporting resources like authors and genres. It also includes user authentication and a feature for book owners to select a recipient if multiple people are interested in a book.

## Features

### User Authentication
- Registration with email
- Login with email and password

### Books Management
- CRUD operations for books
- Filtering books based on author, genre, condition, etc.

### Supporting Resources
- Manage authors, genres, and conditions

### Book Retrieval Information
- Information on the location from where the book can be picked up

### Ownership Decision
- If multiple people are interested in a book, the owner can choose the recipient

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

- Registration: `/register/`
- Login: `/login/`
- Books: `/books/`
- Authors: `/authors/`
- Genres: `/genres/`
- Conditions: `/conditions/`

## Swagger Documentation
- Access the Swagger documentation at `/schema/docs/`

## Contributing

Feel free to fork the project, open a PR, or submit an issue.
