import backend
import customtkinter as ctk


def addtask_gui():
    title = task_entry.get()
    priority = priority_menu.get()
    due_date = date_entry.get()

    success, message = backend.addtask(title, priority, due_date)

    if success:
        status_label.configure(
            text = message,
            text_color = "green"
        )
        task_entry.delete(0,"end")
        priority_menu.set("High")
        date_entry.delete(0,"end")
    else:
        status_label.configure(
            text = message,
            text_color = "red"
        )
    displaytasks()


def complete_task_gui(idx):
    success, message = backend.markAsDone(idx)
    displaytasks()


def pending_task_gui(idx):
    success, message = backend.markAsUndone(idx)
    displaytasks()


def delete_task_gui(idx):
    success, message = backend.deletetask(idx)
    displaytasks()


def search_task_gui():
    keyword = search_entry.get()
    if keyword.strip() == "":
        displaytasks()
        return
    results = backend.search(keyword)
    displaytasks(results)


def update_statistics():
    stats = backend.statistics()
    total_label.configure(
        text= f"Total: {stats['total']}"
    )
    completed_label.configure(
        text= f"Completed: {stats['complete']}"
    )
    pending_label.configure(
        text= f"Pending: {stats['pending']}"
    )
    percentage_label.configure(
        text= f"Percentage completed: {stats['percentage']:.1f}%"
    )


def show_completed_tasks():
    completed_tasks = []
    for task in backend.gettasks():
        if task['completed']:
            completed_tasks.append(task)
    displaytasks(completed_tasks)


def show_pending_tasks():
    pending_tasks = []
    for task in backend.gettasks():
        if not task['completed']:
            pending_tasks.append(task)
    displaytasks(pending_tasks)


def show_high_priority():
    high_tasks = []
    for task in backend.gettasks():
        if task["priority"] == "High":
            high_tasks.append(task)
    displaytasks(high_tasks)


def displaytasks(filtered_tasks=None):
    update_statistics()
    if filtered_tasks is None:
        task_list = backend.gettasks()
    else:
        task_list = filtered_tasks
    for widget in task_frame.winfo_children():
        widget.destroy()
    if not task_list:
        empty_label = ctk.CTkLabel(
            task_frame,
            text="No tasks available"
        )
        empty_label.pack(pady=10)
    for i, task in enumerate(task_list, start=1):
        if task["completed"]:
            status = "✔" 
            status_color = "green"
        else:
            status = "○"
            status_color = "yellow"
        if task["priority"] == "High":
            priority_color = "red"
        elif task["priority"] == "Medium":
            priority_color = "yellow"
        else:
            priority_color = "green"
        card = ctk.CTkFrame(task_frame)
        card.pack(fill='x', padx=10, pady=5)
        # task_label = ctk.CTkLabel(
        #     task_frame,
        #     text= (f"{status} {task['title']}\n"
        #            f"\tPriority: {task['priority']}\n"
        #            f"\tDue Date: {task['due_date']}"),
        #     anchor="w",
        #     justify="left",
        #     font=("Arial", 16)
        # )
        # task_label.pack(anchor="w", padx=10, pady=10)
        top_frame = ctk.CTkFrame(
            card,
            fg_color='transparent'
        )
        top_frame.pack(fill='x', padx=10, pady=(10,0))
        tick_label = ctk.CTkLabel(
            top_frame,
            text= f"{status}",
            text_color=status_color,
            font=("Arial", 18, "bold")
        )
        tick_label.pack(side="left")
        title_label = ctk.CTkLabel(
            top_frame,
            text= f"{task['title']}",
            text_color="white",
            font=("Arial", 16)
        )
        title_label.pack(side="left", padx=5)

        bottom_frame = ctk.CTkFrame(
            card,
            fg_color='transparent'
        )
        bottom_frame.pack(fill='x', padx=10, pady=(0,10))
        priority_label = ctk.CTkLabel(
            bottom_frame,
            text= f"{task['priority']}",
            text_color=priority_color,
            font=("Arial", 12)
        )
        priority_label.pack(side="left", padx=(40,0))
        date_label = ctk.CTkLabel(
            bottom_frame,
            text= f"{task['due_date']}",
            text_color="white",
            font=("Arial", 12)
        )
        date_label.pack(side="left", padx=10)
        button_frame = ctk.CTkFrame(
            card,
            fg_color='transparent'
        )
        button_frame.pack(fill='x', padx=10, pady=(0,10))
        if not task["completed"]:
            done_button = ctk.CTkButton(
                button_frame,
                text="Mark Done",
                fg_color="green",
                hover_color="darkgreen",
                command= lambda i=i: complete_task_gui(i)
            )
            done_button.pack(side="left", padx=10)
        else:
            undone_button = ctk.CTkButton(
                button_frame,
                text="Mark Undone",
                text_color="black",
                fg_color="yellow",
                hover_color="orange",
                command= lambda i=i: pending_task_gui(i)
            )
            undone_button.pack(side="left", padx=10)
        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete",
            fg_color="red",
            hover_color="darkred",
            command= lambda i=i: delete_task_gui(i)
        )
        delete_button.pack(side="left", padx=10)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("ToDo Task Manager")
app.geometry("700x500")

title = ctk.CTkLabel(
    app,
    text = "ToDo Task Manager",
    font = ("Arial", 28, "bold")
)
title.pack(pady=20)

search_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
search_frame.pack(
    anchor='e',
    padx=20,
    pady=10
)
search_entry = ctk.CTkEntry(
    search_frame,
    width=100,
    placeholder_text="Search tasks..."
)
search_entry.pack(side="left", padx=(0,10))
search_button = ctk.CTkButton(
    search_frame,
    width=50,
    text="Search",
    command=search_task_gui
)
search_button.pack(side="left")

stats_frame = ctk.CTkFrame(app)
stats_frame.pack(
    fill="x",
    padx=20,
    pady=10
)
total_label = ctk.CTkLabel(
    stats_frame,
    text="Total: 0",
    font=("Arial", 16, "bold")
)
total_label.pack(
    padx=20
)
completed_label = ctk.CTkLabel(
    stats_frame,
    text="Completed: 0",
    text_color="green",
    font=("Arial", 16, "bold")
)
completed_label.pack(
    padx=20
)
pending_label = ctk.CTkLabel(
    stats_frame,
    text="Pending: 0",
    text_color="yellow",
    font=("Arial", 16, "bold")
)
pending_label.pack(
    padx=20
)
percentage_label = ctk.CTkLabel(
    stats_frame,
    text="Percentage completed: 0%",
    text_color="cyan",
    font=("Arial", 16, "bold")
)
percentage_label.pack(
    padx=20
)

task_entry = ctk.CTkEntry(
    app,
    width = 400,
    placeholder_text = "Enter your task"
)
task_entry.pack(pady=10)

priority_menu = ctk.CTkOptionMenu(
    app,
    values = ["High", "Medium", "Low"]
)
priority_menu.set("High")
priority_menu.pack(pady=10)

date_entry = ctk.CTkEntry(
    app,
    width = 200,
    placeholder_text = "YYYY-MM-DD"
)
date_entry.pack(pady=10)

add_button = ctk.CTkButton(
    app,
    text = "Add Task",
    command=addtask_gui
)
add_button.pack(pady=20)

status_label = ctk.CTkLabel(
    app,
    text=""
)
status_label.pack()

filter_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
filter_frame.pack(fill='x')
all_button = ctk.CTkButton(
    filter_frame,
    text="All",
    fg_color="#344153",
    hover_color="#293341",
    command=displaytasks
)
all_button.pack(
    side="left",
    padx=5
)
completed_button = ctk.CTkButton(
    filter_frame,
    text="Completed",
    fg_color="#344153",
    hover_color="#293341",
    command=show_completed_tasks
)
completed_button.pack(
    side="left",
    padx=5
)
pending_button = ctk.CTkButton(
    filter_frame,
    text="Pending",
    fg_color="#344153",
    hover_color="#293341",
    command=show_pending_tasks
)
pending_button.pack(
    side="left",
    padx=5
)
high_button = ctk.CTkButton(
    filter_frame,
    text="High",
    fg_color="#344153",
    hover_color="#293341",
    command=show_high_priority
)
high_button.pack(
    side="left",
    padx=5
)

task_frame = ctk.CTkScrollableFrame(
    app,
    width=600,
    height=250
)
task_frame.pack(pady=10, fill="both", expand=True)

app.mainloop()