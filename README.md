# ToDo Task Manager

A modern Python-based task management application featuring both a Command-Line Interface (CLI) and a Graphical User Interface (GUI) built using CustomTkinter.

The project focuses on clean architecture, modular backend/frontend separation, persistent storage, interactive GUI design, and scalable software engineering principles.

---

# Features

## CLI Features

- Add tasks
- Delete tasks
- Mark tasks as completed
- Mark tasks as pending
- Search tasks
- View task statistics
- Colored terminal interface using Colorama

---

## GUI Features

- Modern dark-themed GUI using CustomTkinter
- Dynamic task rendering
- Scrollable task list
- Search functionality
- Task filtering system
- Statistics dashboard
- Mark done / mark undone
- Delete tasks
- Colored priority indicators
- Real-time UI updates

---

# Task Structure

Each task stores:

- Title
- Completion status
- Priority
- Due date

Example:

```json
{
    "title": "Study Python",
    "completed": false,
    "priority": "High",
    "due_date": "2026-05-30"
}
```

---

# Project Architecture

```text
todo_app/
│
├── backend.py
├── main.py
├── gui.py
├── tasks.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

## Current Stack

- Python 3
- CustomTkinter
- Colorama
- JSON Storage
- File Handling

---

# Software Design Concepts

This project demonstrates:

- Modular programming
- Backend/frontend separation
- Event-driven GUI programming
- State management
- Dynamic UI rendering
- Search and filtering systems
- Persistent local storage
- Reactive interface updates
- Input validation
- Software architecture principles

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/todo-cli.git
```

Move into project directory:

```bash
cd todo-cli
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

## Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the CLI Version

```bash
python main.py
```

---

# Running the GUI Version

```bash
python gui.py
```

---

# Future Improvements

- SQLite database integration
- User authentication
- Task categories
- Task editing
- Drag-and-drop task management
- Cloud synchronization
- Flask web version

---

# Repository Status

Current Version: GUI + CLI Application  
Architecture: Modular Backend/Frontend  
GUI Framework: CustomTkinter

---

# License

This project is licensed under the MIT License.