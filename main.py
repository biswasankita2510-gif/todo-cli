from backend import *
from colorama import Fore, Style, init
init(autoreset=True)



def viewtask_cli():
    task_list = gettasks()
    print("\n" + "-"*30)
    print(" YOUR TASK LIST ")
    print("-"*30)

    if not task_list:
        print(Fore.RED + "⚠ No tasks to print.")
        return
    for i, task in enumerate(task_list, start=1): 
        status = (
            f"{Fore.GREEN}✔{Style.RESET_ALL}" 
            if task['completed'] 
            else f"{Fore.YELLOW} {Style.RESET_ALL}"
        )
        if task['priority'] == "High":
            prio_col = Fore.RED 
        elif task['priority'] == "Medium":
            prio_col = Fore.YELLOW
        else:
            prio_col = Fore.GREEN
        print(f"{i}. [{status}] {task['title']} |"
              f" Priority: {prio_col}{task['priority']}{Style.RESET_ALL} | "
              f"Due: {task['due_date']}") 
    print("_"*30 + "\n") 


def addtask_cli():
    title = input("Enter task: ").strip()
    priority = input("Enter priority: ").capitalize()
    due_date = input("Enter due date: ").strip()
    success, message = addtask(title, priority, due_date)

    if success:
        print(Fore.GREEN + message)

    else:
        print(Fore.RED + message)


def markAsDone_cli():
    viewtask_cli()
    idx = int(input("Enter the index of the task you want to mark as done (✔): "))
    success, message = markAsDone(idx)
    if not success:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)
  

def markAsUndone_cli():
    viewtask_cli()
    idx = int(input("Enter the index of the task you want to mark as undone (✔): "))
    success, message = markAsUndone(idx)
    if not success:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)
            

def search_cli():
    keyword = input("Enter the keyword: ")
    result = search(keyword)
    if not result:
        print(Fore.RED + "No matching result")
        return
    print("\n" + "-"*30 + "\n" + " Search Result " + "\n" + "-"*30)
    for i, task in enumerate(result, start=1):
        print(f"{i}. {task['title']}")
    print("_"*30 + "\n")


def deletetask_cli():
    viewtask_cli()
    idx = int(input("Enter the index of the task you want to delete: "))
    success, message = deletetask(idx)
    if not success:
        print(Fore.RED + message)
    else:
        print(Fore.GREEN + message)


def statistics_cli():
    stats = statistics()
    if not stats:
        print(Fore.RED + "⚠ No tasks available.")
    print("\n" + "-"*30)
    print(" TASK STATISTICS ")
    print("-"*30)
    print(f"Total Tasks      : {stats['total']}")
    print(f"Completed Tasks  : {Fore.GREEN}{stats['complete']}")
    print(f"Pending Tasks    : {Fore.RED}{stats['pending']}")
    print(f"Completion Rate  : {Fore.CYAN}{stats['percentage']:.1f}%")
    print("_"*30 + "\n")
    

while True:
    try:
        choice = int(input("\nChoose an option:\n1 -> View Tasks\n2 -> Add Task\n3 -> Delete Task\n4 -> Mark As Done\n5 -> Mark As Undone\n6 -> Search\n7 -> Statistics\n8 -> Exit\nEnter your choice: "))
    except ValueError:
        print("⚠ Invalid input.\nEnter a no. between 1-8.")
        continue
    if(choice == 1):
        viewtask_cli()
    elif(choice == 2):
        addtask_cli()
    elif(choice == 3):
        deletetask_cli()
    elif(choice == 4):
        markAsDone_cli()
    elif(choice == 5):
        markAsUndone_cli()
    elif(choice == 6):
        search_cli()
    elif(choice == 7):
        statistics_cli()
    elif(choice == 8):
        print("Exiting...")
        break
    else:
        print("⚠ Invalid choice...Try again please")