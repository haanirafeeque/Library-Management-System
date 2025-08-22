[README.md](https://github.com/user-attachments/files/21941749/README.md)
# 📚 Library Management System (Python + MySQL)

This is a **Library Management System** built using **Python** and
**MySQL** that allows users and administrators to manage library
operations digitally.\
It provides a simple command-line interface for users to borrow, return,
and search books, while admins can manage membership and view book
records.

------------------------------------------------------------------------

## 🚀 Features

### 👨‍🎓 User Features

-   Register as a new member with personal details.
-   Secure login system with username and password.
-   View personal membership details.
-   Search books by:
    -   Title\
    -   Author\
    -   Genre\
    -   Availability status
-   Borrow and return books with automatic status updates.
-   View all books borrowed by the user.

### 🛠️ Admin Features

-   Secure admin login.
-   View all available books.
-   View all borrowed books.
-   View all library members.
-   Delete a membership when required.
-   Filter books by author or genre.

------------------------------------------------------------------------

## 🗄️ Database Schema (MySQL)

The project uses a **MySQL database** with the following tables:

-   **MEMBER_INFO** → Stores member details (Name, Age, Country, State,
    Phone, Email).\
-   **BOOK_RECORDS** → Stores records of borrowed books.\
-   **ALL_BOOKS** → Stores all books in the library with details (Book
    No, Name, Author, Genre, Status).\
-   **USERS** → Stores login credentials of registered members.

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   **Python 3**\
-   **MySQL Connector for Python**\
-   **MySQL Database**

------------------------------------------------------------------------

## ▶️ How to Run

1.  Install MySQL and create a database named `library`.\

2.  Run the following SQL commands to set up tables:

    ``` sql
    CREATE DATABASE LIBRARY;
    USE LIBRARY;

    CREATE TABLE MEMBER_INFO (NAME varchar(20), AGE int, Country varchar(40), STATE varchar(50), Phone_No bigint, Email varchar(40));
    CREATE TABLE BOOK_RECORDS (NAME varchar(20), BOOK_NAME VARCHAR(50), DATE_BORROWED date, DATE_RETURNED date);
    CREATE TABLE ALL_BOOKS(BOOK_NO INT, BOOK_NAME VARCHAR(50), AUTHOR VARCHAR(50), GENRE VARCHAR(50), STATUS VARCHAR(20) DEFAULT 'AVAILABLE');
    CREATE TABLE USERS(NAME varchar(20), PASSWORD varchar(20));
    ```

3.  Update the database connection in the code if needed:

    ``` python
    con = mysql.connector.connect(host='localhost', user='root', password='your_password', database='library')
    ```

4.  Run the script:

    ``` bash
    python CS_PROJECT_SOURCE_CODE.py
    ```

------------------------------------------------------------------------

## 📌 Author

Developed as a **Computer Science project** for managing library
operations using Python and MySQL.
