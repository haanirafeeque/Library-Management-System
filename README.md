# Library Management System (Python + MySQL)!

This is a **Library Management System** built using **Python** and
**MySQL** that allows users and administrators to manage library
operations digitally.
It provides a simple command-line interface for users to borrow, return,
and search books, while admins can manage membership and view book
records.

------------------------------------------------------------------------

## Features

### User Features:

-   Register as a new member with personal details.
-   Secure login system with username and password.
-   View personal membership details.
-   Search books by:
    -   Title
    -   Author
    -   Genre
    -   Availability status
-   Borrow and return books with automatic status updates.
-   View all books borrowed by the user.

### Admin Features:

-   Secure admin login.
-   View all available books.
-   View all borrowed books.
-   View all library members.
-   Delete a membership when required.
-   Filter books by author or genre.

------------------------------------------------------------------------

## Database (MySQL)

The project uses a **MySQL database** with the following tables:

-   **MEMBER_INFO** → Stores member details (Name, Age, Country, State,
    Phone, Email).
-   **BOOK_RECORDS** → Stores records of borrowed books.
-   **ALL_BOOKS** → Stores all books in the library with details (Book
    No, Name, Author, Genre, Status).
-   **USERS** → Stores login credentials of registered members.

------------------------------------------------------------------------

## Languages Used and Modules used

-   **Python 3**
-   **MySQL Connector for Python**
-   **MySQL Database**

------------------------------------------------------------------------

This project was made as a **Computer Science project** for grade XII by using MySQL and Python!
