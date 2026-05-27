import json
from datetime import datetime


tasks = []
def loadtask():
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []


def savetask():
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def addtask(title, priority, due_date):
    if title.strip() == "":
        return False, "⚠ Tasks cannot be empty."
    if priority not in ["High", "Medium", "Low"]:
        return False, "⚠ Add proper priority"
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return False, "⚠ Invalid date format"
    task = {
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    savetask()
    return True, "✔ Task added successfully"


def gettasks():
    return tasks


def markAsDone(idx):
    if (not tasks):
        return False, "⚠ No tasks available."
    if not (1 <= idx <= len(tasks)):
        return False, "⚠ Invalid index"
    if(tasks[idx-1]['completed']):
        return False, "Task already completed ✔"
    tasks[idx-1]['completed'] = True
    savetask()
    return True, "Task marked done"


def markAsUndone(idx):
    if (not tasks):
        return False, "⚠ No tasks available."
    if not (1 <= idx <= len(tasks)):
        return False, "⚠ Invalid index"
    if not (tasks[idx-1]['completed']):
        return False, "Task already pending"
    tasks[idx-1]['completed'] = False
    savetask()
    return True, "Task marked undone"


def deletetask(idx):
    if (not tasks):
        return False, "⚠ No tasks to delete."
    if not (1 <= idx <= len(tasks)):
        return False, "⚠ Invalid index"
    popped = tasks.pop(idx-1)
    savetask()
    return True, f"{idx}. {popped['title']} (deleted)"


def search(keyword):
    result = []
    for task in tasks:
        if keyword.lower() in task['title'].lower():
            result.append(task)
    return result


def statistics():
    # if not tasks:
    #     return False, "⚠ No tasks available."
    total = len(tasks)
    complete = sum(task['completed'] for task in tasks)
    pending = total-complete
    percentage = (complete / total) * 100 if total > 0 else 0
    return {
        "total":total,
        "complete": complete,
        "pending": pending,
        "percentage": percentage
    }

loadtask()