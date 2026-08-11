# Student-Management-System
# Student Management System

A simple desktop-based **Student Management System** developed using **Python, Tkinter, and SQLite**. The application provides a graphical interface to manage student records with basic CRUD operations.

## Features

* Add new student records
* View all student records
* Update existing student information
* Delete student records
* Clear input fields
* Prevent duplicate roll numbers
* Store student data permanently using SQLite
* Simple and user-friendly Tkinter GUI

## Technologies Used

* **Python**
* **Tkinter** – GUI development
* **SQLite** – Database management
* **SQL** – Database queries

## Project Structure

```text
Student-Management-System/
│
├── student_management.py
├── README.md
└── students.db
```

> `students.db` may be created automatically when the application is executed for the first time.

## Requirements

* Python 3.x
* Tkinter
* SQLite

Tkinter and SQLite are included with most standard Python installations, so no additional database server is required.

## How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Student-Management-System
```

### 3. Run the Application

```bash
python student_management.py
```

The Student Management System GUI will open.

## How It Works

The application provides fields for entering student information such as:

* Roll Number
* Student Name
* Course
* Fees

Users can perform the following operations:

**Add:** Adds a new student to the database.

**View:** Displays stored student records in the application.

**Update:** Updates the selected student's information.

**Delete:** Removes the selected student record.

**Clear:** Clears the input fields.

## Database

The application uses **SQLite** to store student information.

SQLite is a lightweight, file-based relational database that does not require a separate database server.

## Learning Outcomes

Through this project, I practiced:

* Python programming
* Object-oriented and functional programming concepts
* Tkinter GUI development
* SQLite database integration
* SQL CRUD operations
* Event handling
* Exception handling
* Basic application development

## Future Improvements

The project can be enhanced with:

* Student search functionality
* Input validation
* Login and authentication
* Student profile management
* Export records to CSV/Excel
* Improved GUI design
* Attendance management
* Fee payment tracking

## Author

**Phanishree N.M.**

MCA (Pursuing) | BCA Graduate
Python | SQL | Java | Django | Flask

---

## License

This project is created for learning and educational purposes.
