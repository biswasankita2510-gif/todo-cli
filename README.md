# To-Do Application

A Python-based task management application built as a Command Line Interface (CLI) system, with planned upgrades to a modern GUI and web-based application.

This project focuses on modular programming, persistent storage, task state management, and scalable application design while keeping the code clean, beginner-friendly, and maintainable.

---

## Preview

```text
------------------------------
 YOUR TASK LIST
------------------------------
1. [ ] Complete Python project
2. [✔] Push project to GitHub
______________________________
```

---

## Current Features

| Feature | Description |
|---|---|
| Add Tasks | Create and save new tasks |
| Delete Tasks | Remove tasks from the list |
| Mark as Done | Mark tasks as completed |
| Mark as Undone | Revert completed tasks |
| Search Tasks | Find tasks using keywords |
| Persistent Storage | Tasks are automatically saved locally |
| Error Handling | Handles invalid input safely |
| Unicode Support | Supports UTF-8 file operations |

---

## Project Structure

```text
todo-cli-python/
│
├── main.py
├── tasks.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

### Current Stack

- Python 3
- File Handling
- Lists and String Manipulation

### Planned Stack

- CustomTkinter
- Flask
- SQLite / PostgreSQL

---

## How It Works

The application stores tasks inside a local text file (`tasks.txt`) and automatically loads them during startup.

Each task maintains a completion state:

```text
[ ] Pending Task
[✔] Completed Task
```

The project uses modular functions to separate functionalities such as:

- Adding tasks
- Deleting tasks
- Searching tasks
- Updating task status
- Saving and loading data

This structure improves readability and makes future upgrades easier.

---

## Running the Application

### Clone the Repository

```bash
git clone https://github.com/your-username/todo-cli-python.git
```

### Move into the Project Directory

```bash
cd todo-cli-python
```

### Run the Application

```bash
python main.py
```

---

## Learning Outcomes

This project helped strengthen understanding of:

- Modular programming
- File handling in Python
- Input validation
- Exception handling
- String manipulation
- Search functionality
- State management
- Debugging techniques
- Git and GitHub workflow

---

## Future Development Roadmap

### Phase 1 — CLI Application

- Basic task management system
- Persistent local storage
- Task completion tracking

### Phase 2 — GUI Application

Planned improvements:

- Modern desktop interface using CustomTkinter
- Interactive task controls
- Scrollable task list
- Search bar integration
- Improved user experience

### Phase 3 — Web Application

Planned improvements:

- Flask-based web application
- Database integration
- Authentication system
- Task categorization and prioritization
- Responsive UI design

---

## Possible Future Improvements

- Due dates and deadlines
- Task priorities
- Colored terminal interface
- Export tasks to CSV/JSON
- Notification/reminder system
- Dark mode GUI
- Cloud synchronization

---

## Repository Status

| Component | Status |
|---|---|
| CLI Application | Completed |
| GUI Version | Planned |
| Web Version | Planned |

---

## License

This project is open-source and available under the MIT License.