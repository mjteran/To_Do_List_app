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
# create global variables:
task_l = []

# create functions:
def add_task(task):
    task_l.append(task)
    print(f"'{task}' has been added to list.")



def view_task():
    n = 1
    print("To-Do List:")
    for i in task_l:
       print(f"{n}. {i}")
       n += 1
#remove
def remove_task():
    if not task_l:
        print("The To-do List is empty.")
        return main()

    task = input("Enter the task to remove: ")
    if task in task_l:
        task_l.remove(task)
        print(f"'{task}' has been removed from list.")
    else:
        print("The task is not in the list")
        e = input("You want to try another task: 'Y' to retry, any else character to return to menu:")
        if e in "Yy":
            return remove_task()
def mark_task():
    if not task_l:
        print("The To-do List is empty.")
        return main()
    v = input("Enter the complete task:").strip()
    if v in task_l:
        c = task_l.index(f"{v}")
        task_l[c] = f"{v} (completed)"
        print(f"{v} has been marked complete.")
    else:
        print("The task is not in the list")
        e = input("You want to try another task: 'Y' to retry, any else character to return to menu:")
        if e in "Yy":
            return mark_task()
# create a menu to start the TDL 1 App:
def main():
    while True:
        print("To - Do List Application:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark complete task")
        print("5. Exit")
        request = input("Enter your choice: ")
        if request == "1":
            task = input("Enter the task to add: ")
            print(task)
            add_task(task)
        elif request == "2":
            remove_task()
        elif request == "3":
            print("The existing tasks are the following: ")
            view_task()
        elif request == "4":
            mark_task()
        elif request == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# call the main menu
main()

