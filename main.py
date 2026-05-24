def loadtask():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


def savetask():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


def viewtask():
    print("\n" + "-"*30)
    print(" YOUR TASK LIST ")
    print("-"*30)
    if (not tasks):
        print("⚠ No tasks to print.")
        return
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    print("_"*30 + "\n")


def addtask():
    task = input("Enter the task: ").strip()
    if task == "":
        print("⚠ Tasks cannot be empty.")
        return
    task = "[ ] " + task #adding status
    tasks.append(task)
    print("✔ Task adding successful")
    savetask()


def markAsDone():
    if (not tasks):
        print("⚠ No tasks available.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to mark as done (✔): "))
        if (1 <= idx <= len(tasks)):
            if(tasks[idx-1].startswith("[✔]")):
                print("Task already completed ✔")
            else:
                task = tasks[idx-1][4:]
                # tasks[idx-1] = tasks[idx-1].replace("[ ]", "[✔]", 1)
                tasks[idx-1] = "[✔] " + task
                savetask()
                print(f"Task {task} marked done")
                viewtask()
        else:
            print("⚠ Invalid index")
    except ValueError:
        print("⚠ Enter valid index (Starts from 1).")
        return
    

def markAsUndone():
    if (not tasks):
        print("⚠ No tasks available.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to mark as undone (✔): "))
        if (1 <= idx <= len(tasks)):
            if(tasks[idx-1].startswith("[ ]")):
                print("Task already not completed")
            else:
                task = tasks[idx-1][4:]
                # tasks[idx-1] = tasks[idx-1].replace("[ ]", "[✔]", 1)
                tasks[idx-1] = "[ ] " + task
                savetask()
                print(f"{task} (marked undone)")
                viewtask()
        else:
            print("⚠ Invalid index")
    except ValueError:
        print("⚠ Enter valid index (Starts from 1).")
        return
            

def search():
    if not tasks:
        print("No tasks available")
    keyword = input("Enter the keyword to search: ").lower()
    found = False
    print("\n" + "-"*30 + "\n" + " Search Result " + "\n" + "-"*30)
    for i, task in enumerate(tasks, start=1):
        if keyword in task.lower():
            print(f"{i}. {task}")
            found = True
    if not found:
        print(f"No task found with keyword {keyword}")
    print("_"*30 + "\n")


def deletetask():
    if (not tasks):
        print("⚠ No tasks to delete.")
        return
    viewtask()
    try:
        idx = int(input("Enter the index of the task you want to delete: "))
        if (0 < idx <= len(tasks)):
            popped = tasks.pop(idx-1)
            savetask()
            print(f"✔ Task ({idx}. {popped}) deleted.")
        else:
            print("⚠ Invalid index")
    except ValueError:
        print("⚠ Enter valid index (Starts from 1).")


tasks = []
loadtask()
viewtask()
while True:
    try:
        choice = int(input("\nChoose an option:\n1 -> View Tasks\n2 -> Add Task\n3 -> Delete Task\n4 -> Mark As Done\n5 -> Mark As Undone\n6 -> Search\n7 -> Exit\nEnter your choice: "))
    except ValueError:
        print("⚠ Invalid input.\nEnter a no. between 1-5.")
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
        print("Exiting...")
        break
    else:
        print("⚠ Invalid choice...Try again please")