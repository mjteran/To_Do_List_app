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


# create a menu to start the TDL 1 App:
def main():
    while True:
        print("To - Do List Application:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
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
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# call the main menu
main()