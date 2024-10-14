# To-Do List Application 1 - Group 7
#   - Sebastian
#   - Maria Jose

# Objective:
# Create a simple to-do list application that allows users to add, remove, and view tasks.
# The application will provide a menu for the user to perform the following actions:
# 1. Add a task to the to-do list.
# 2. Remove a task from the to-do list.
# 3. View all tasks in the to-do list.
# 4. Exit the application.

# to-do list application coding:
# global variables:
task_l = []
changes_unsaved = False

# functions:
# function to add tasks to the list:
def task_exists(task):
    for existing_task in task_l:                        # verify tasks in task list
        if existing_task.lower().replace(" (completed)", "") == task.lower():   # verify the original task
            return existing_task                        # return the matching task
    return None                                         # return None if no matching task is found

def add_task(task):
    global changes_unsaved
    if task_exists(task):                               # validate if task already exists
        print(f"'{task}' is already in the list. Duplicate tasks are not allowed.\n")
    else:
        task_l.append(task)                             # append task to the list
        changes_unsaved = True                          # flag to indicate changes
        print(f"'{task}' has been added to list.\n")

# function to view all tasks:
def view_task():
    if not task_l:                                      # if the list of tasks is empty
        print("The To-do List is empty.\n")
        return
    print("To-do List:")
    for n, task in enumerate(task_l, start=1):          # enumerate tasks starting from 1
        print(f"{n}. {task}")
    print()

# function to remove a task:
def remove_task():
    global changes_unsaved
    if not task_l:                                      # if list of tasks is empty and nothing to remove
        print("The To-do List is empty.\n")
        return

    task = input("Enter the task to remove: ").strip()  # remove extra spaces in the task
    if task == "":                                      # validate if task to remove is empty
        print("Invalid input. Task cannot be empty.\n")
        return

    existing_task = task_exists(task)                   # check if the task exists
    if existing_task:                                   # if a matching task
        task_l.remove(existing_task)                    # remove the task
        changes_unsaved = True                          # flag to indicate changes
        print(f"'{task}' has been removed from the list.\n")
    else:                                               # if task is not in the list
        print(f"The task '{task}' is not in the list. Please ensure the task matches exactly.")
        retry = input("Would you like to try again? ('Y' to retry, any other character to return to the menu):")
        if retry.lower() == 'y':                        # to retry if failing
            remove_task()

# function to save the task list to a file
def save_tasks(filename='tasks.txt'):
    global changes_unsaved
    if not task_l:                                      # if list of tasks is empty
        print("The To-do List is empty. No file saved.\n")
        return
    with open(filename, 'w') as file:                   # open file tasks.txt
        for task in task_l:
            file.write(f"{task}\n")                     # write tasks in the file
    print(f"Tasks saved to {filename}.\n")
    changes_unsaved = False

# function to load the task list from a file
def load_tasks(filename='tasks.txt'):                   # load the tasks file
    new_task = 0
    try:
        with open(filename, 'r') as file:               # read the tasks
            for line in file:
                task = line.strip()
                if task and task not in task_l:         # avoid duplicates
                    task_l.append(task)                 # to avoid duplicates
                    new_task += 1                       # count new tasks
        if new_task > 0:
            print(f"{new_task} Task(s) were loaded from {filename}.\n")
            return
        else:
            print("The file was read, but no tasks were loaded.\n")
    except FileNotFoundError:                           # error if file not found or not tasks
        print(f"File '{filename}' not found.\n")

# function to mark a task as completed
def mark_task():
    if not task_l:                                                      # task list empty
        print("The To-do List is empty.\n")
        return
    task_c = input("Enter the completed task: ").strip().lower()
    existing_task = task_exists(task_c)                                 # validate if task already exists
    if existing_task:
        if "(completed)" not in existing_task:                          # mark the task as completed
            task_l[task_l.index(existing_task)] += " (completed)"
            print(f"'{task_c}' has been marked as completed.\n")
        else:                                                           # task already marked as completed
            print(f"'{task_c}' is already marked as completed.\n")
    else:
        print(f"The task '{task_c}' is not in the list.")               # task not found in the list
        retry = input("Would you like to try again? ('Y' to retry, any other character to return to the menu): ")
        if retry.lower() == 'y':
            mark_task()

def main():
    while True:
        print("To - Do List Application:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark complete task")
        print("5. Load Tasks list from a File")
        print("6. Save Tasks to a File")
        print("7. Exit")
        request = input("Enter your choice: ").strip()      # remove extra spaces in the task
        # validate options
        if request == "1":
            task = input("Enter the task to add: ").strip() # remove extra spaces in the task
            if task:                                        # check if the input is not empty
                add_task(task)
            else:                                           # validate if new task is empty
                print("Invalid input. Task cannot be empty.\n")
        elif request == "2":
            remove_task()
        elif request == "3":
            view_task()
        elif request == "4":
            mark_task()
        elif request == "5":
            load_tasks()
        elif request == "6":
            save_tasks()
        elif request == "7":
            if changes_unsaved:
                save_user = input("You have unsaved changes. Would you like to save before exiting? (Y/N): ").strip().lower()
                if save_user == 'y':
                    save_tasks()                        # save changes if user chooses
                elif save_user != 'n':
                    print("Invalid choice. Exiting without saving.")
            print("Exiting the application. Goodbye!")
            break
        else:                                           # validate wrong inputs
            print("Invalid choice. Please try again.\n")

# call the main menu
main()