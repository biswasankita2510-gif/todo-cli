import json
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)

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


def viewtask():
    print("\n" + "-"*30)
    print(" YOUR TASK LIST ")
    print("-"*30)
    if (not tasks):
        print(Fore.RED + "⚠ No tasks to print.")
        return
    for i, task in enumerate(tasks, start=1):
        status = f"{Fore.GREEN}✔{Style.RESET_ALL}" if task['completed'] else f"{Fore.YELLOW} {Style.RESET_ALL}"
        if task['priority'] == "High":
            prio_col = Fore.RED
        elif task['priority'] == "Med":
            prio_col = Fore.YELLOW
        else:
            prio_col = Fore.GREEN
        print(f"{i}. [{status}] {task['title']} |"
              f" Priority: {prio_col}{task['priority']}{Style.RESET_ALL} | "
              f"Due: {task['date']}")
    print("_"*30 + "\n")


def addtask():
    title = input("Enter the task: ").strip()
    prior = input("Enter the priority of the task (High/Med/Low): ").capitalize()
    date = input("Enter the due date (YYYY-MM-DD): ").strip()
    if title == "":
        print(Fore.RED + "⚠ Tasks cannot be empty.")
        return
    if prior not in ["High", "Med", "Low"]:
        print(Fore.RED + "⚠ Add proper priority")
        return
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "⚠ Invalid date format")
        return
    task = {
        "title": title,
        "completed": False,
        "priority": prior,
        "date": date
    }
    tasks.append(task)
    savetask()
    print(Fore.GREEN + "✔ Task added successfully")


def markAsDone():
    if (not tasks):
        print(Fore.RED + "⚠ No tasks available.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to mark as done (✔): "))
        if (1 <= idx <= len(tasks)):
            if(tasks[idx-1]['completed']):
                print(Fore.GREEN + "Task already completed ✔")
            else:
                tasks[idx-1]['completed'] = True
                savetask()
                print(Fore.GREEN + f"✔ {tasks[idx-1]['title']} marked done")
                viewtask()
        else:
            print(Fore.RED + "⚠ Invalid index")
    except ValueError:
        print(Fore.RED + "⚠ Enter valid index (Starts from 1).")
        return
    

def markAsUndone():
    if (not tasks):
        print(Fore.RED + "⚠ No tasks available.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to mark as undone (✔): "))
        if (1 <= idx <= len(tasks)):
            if not (tasks[idx-1]['completed']):
                print(Fore.RED + "Task already not completed")
            else:
                tasks[idx-1]['completed'] = False
                savetask()
                print(Fore.YELLOW + f"↩ {tasks[idx-1]['title']} marked undone")
                viewtask()
        else:
            print(Fore.RED + "⚠ Invalid index")
    except ValueError:
        print(Fore.RED + "⚠ Enter valid index (Starts from 1).")
        return
            

def search():
    if not tasks:
        print(Fore.RED + "⚠ No tasks available")
        return
    keyword = input("Enter the keyword to search: ").lower()
    found = False
    print("\n" + "-"*30 + "\n" + " Search Result " + "\n" + "-"*30)
    for i, task in enumerate(tasks, start=1):
        if keyword in task['title'].lower():
            status = "✔" if task['completed'] else " "
            print(f"{i}. [{status}] {task["title"]} | Priority: {task['priority']} | Due: {task['date']}")
            found = True
    if not found:
        print(f"No task found with keyword {keyword}")
    print("_"*30 + "\n")


def deletetask():
    if (not tasks):
        print(Fore.RED + "⚠ No tasks to delete.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to delete: "))
        if (0 < idx <= len(tasks)):
            popped = tasks.pop(idx-1)
            savetask()
            print(f"✔ Task ({idx}. {popped['title']}) deleted.")
        else:
            print(Fore.RED + "⚠ Invalid index")
    except ValueError:
        print(Fore.RED + "⚠ Enter valid index (Starts from 1).")


def statistics():
    if not tasks:
        print(Fore.RED + "⚠ No tasks available.")
        return
    total = len(tasks)
    complete = sum(task['completed'] for task in tasks)
    pending = total-complete
    percentage = (complete / total) * 100 if total > 0 else 0
    print("\n" + "-"*30)
    print(" TASK STATISTICS ")
    print("-"*30)
    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {Fore.GREEN}{complete}")
    print(f"Pending Tasks    : {Fore.RED}{pending}")
    print(f"Completion Rate  : {Fore.CYAN}{percentage:.1f}%")
    print("_"*30 + "\n")


tasks = []
loadtask()
viewtask()
while True:
    try:
        choice = int(input("\nChoose an option:\n1 -> View Tasks\n2 -> Add Task\n3 -> Delete Task\n4 -> Mark As Done\n5 -> Mark As Undone\n6 -> Search\n7 -> Statistics\n8 -> Exit\nEnter your choice: "))
    except ValueError:
        print("⚠ Invalid input.\nEnter a no. between 1-8.")
        continue
    if(choice == 1):
        viewtask()
    elif(choice == 2):
        addtask()
    elif(choice == 3):
        deletetask()
    elif(choice == 4):
        markAsDone()
    elif(choice == 5):
        markAsUndone()
    elif(choice == 6):
        search()
    elif(choice == 7):
        statistics()
    elif(choice == 8):
        print("Exiting...")
        break
    else:
        print("⚠ Invalid choice...Try again please")