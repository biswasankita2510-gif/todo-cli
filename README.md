# ToDo CLI

A modular Python CLI-based task management application with persistent storage, task state management, and future GUI/web expansion plans.

---

# Features

- Add Tasks
- Delete Tasks
- Mark Tasks as Completed
- Mark Tasks as Undone
- Search Tasks
- Persistent Local Storage
- Input Validation and Error Handling
- Unicode-Safe File Operations

---

# Preview

```text
------------------------------
 YOUR TASK LIST
------------------------------
1. [ ] Complete Python project
2. [✔] Push project to GitHub
______________________________
```

---

# Project Structure

```text
todo-cli/
│
├── main.py
├── tasks.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

## Current Stack

- Python 3
- File Handling
- Lists
- String Manipulation

## Planned Stack

- CustomTkinter
- Flask
- SQLite / PostgreSQL

---

# How It Works

The application stores tasks inside a local text file (`tasks.txt`) and automatically loads them during startup.

Each task maintains a completion state:

```text
[ ] Pending Task
[✔] Completed Task
```

The project is designed using modular functions for:

- Task creation
- Task deletion
- Searching tasks
- Updating task states
- Saving and loading data

This structure improves readability, maintainability, and future scalability.

---

# Running the Application

## Clone the Repository

```bash
git clone https://github.com/your-username/todo-cli.git
```

---

## Move Into the Project Directory

```bash
cd todo-cli
```

---

## Run the Application

```bash
python main.py
```

---

# Learning Outcomes

This project helped strengthen understanding of:

- Modular Programming
- File Handling in Python
- Input Validation
- Exception Handling
- State Management
- Search Functionality
- Debugging Techniques
- Git and GitHub Workflow

---

# Future Development Roadmap

## Phase 1 — CLI Application

- Basic task management system
- Persistent storage
- Task completion tracking

---

## Phase 2 — GUI Application

Planned improvements:

- Modern desktop interface using CustomTkinter
- Interactive task controls
- Scrollable task list
- Search bar integration
- Improved user experience

---

## Phase 3 — Web Application

Planned improvements:

- Flask-based web application
- Database integration
- Authentication system
- Task categorization
- Responsive UI

---

# Possible Future Improvements

- Due dates and deadlines
- Task priorities
- Colored terminal interface
- Export tasks to CSV/JSON
- Reminder system
- Dark mode GUI
- Cloud synchronization

---

# Repository Status

| Component | Status |
|---|---|
| CLI Application | Completed |
| GUI Version | Planned |
| Web Version | Planned |

---

# License

This project is open-source and available under the MIT License.