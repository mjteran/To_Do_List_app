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
#Import the main libraries
from datetime import datetime
import pandas as pd

# global variables:
task_l = []
task_df = pd.DataFrame(columns=['Task','Priority', 'Date', 'Priority_Value',"Complete"])
changes_unsaved = False
# priorities:
p_value = {'high': 1, 'medium': 2, 'low': 3}
print(datetime.today())
# functions:
# function to add tasks to the list:
def add_task(task):
    global changes_unsaved, p_value, task_df
    if task in task_df['Task'].values:                           # validate if task already exists
        print(f"'{task}' is already in the list. Duplicate tasks are not allowed.\n")
        return
    allow = ["high", "medium", "low"]
    while True:                                                 # determine if the priority is acceptable
        p = input("Enter the priority (high,medium,low):").strip().lower()
        if p in allow:
            break
        else:
            print("Not valid priority, please try again.")

    f = "%Y-%m-%d"                                              # date format
    while True:                                                 # determine if the date is acceptable
        day = input("Enter the deadline (YYYY-MM-DD):")
        try:
            v = datetime.date(datetime.strptime(day,f))
            if v < datetime.date(datetime.today()):  # Check if the date is not prior of the entry date
                print(v)
                print("Invalid date entered. Deadline can't be in the past. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date entered. Please try again.")
    # add new task as a row
    new_task = {'Task':task,'Priority':p, 'Date':v, 'Priority_Value':p_value[p], 'Complete': "No"}
    task_l.append(new_task)
    task_df.loc[len(task_df)] = new_task  # append the new task as a row
    print(task_df)
    changes_unsaved = True                                      # flag to indicate changes
    print(f"'{task}' has been added to list.\n")

def view_task():
    if task_df.empty:                                            # if the list of tasks is empty
        print("The To-do List is empty.\n")
        return

    task_df['Date'] = pd.to_datetime(task_df['Date'])             # 'Date' to datetime for sorting
    # first sort by Date
    task_df.sort_values(by=['Date'], ascending=True, inplace=True)           # sort 'Date' in ascending order
    # second sort by Priority
    task_sorted = task_df.sort_values(by=['Priority_Value'])         # sort by Priority values
    print(task_sorted[["Task",'Priority',"Date","Complete"]])

# function to remove a task:
def remove_task():
    global changes_unsaved
    if task_df.empty:                                      # if list of tasks is empty and nothing to remove
        print("The To-do List is empty.\n")
        return

    task = input("Enter the task to remove: ").strip()  # remove extra spaces in the task
    if task == "":                                      # validate if task to remove is empty
        print("Invalid input. Task cannot be empty.\n")
        return

    if task in task_df["Task"].values:                                  # to remove task
        task_df.drop(task_df[task_df["Task"]==task].index,inplace=True)   #Remove the entire row that match with the task condition
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
    if not task_l:  # if list of tasks is empty
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
                task = line.strip().strip('[]').split(",") # split by comma
                if len(task) == 3:                      # 3 columns
                    task, priority, date = task
                    if task and task not in task_df['Task'].values:  # avoid duplicates
                        task_df.loc[len(task_l)] = [task.strip(), priority.strip(), date.strip(), p_value[priority.strip()]]  # append as list
                        new_task += 1                   # count new tasks

        if new_task > 0:
            print(f"{new_task} Task(s) were loaded from {filename}.\n")
            return
        else:
            print("The file was read, but no tasks were loaded.\n")
    except FileNotFoundError:                           # error if file not found or not tasks
        print(f"File '{filename}' not found.\n")

# function to mark a task as completed
def mark_task():
    if not task_l:
        print("The To-do List is empty.")
        return
    v = input("Enter the complete task:").strip()
    if v in task_df["Task"].values:
        task_df.loc[task_df["Task"] == v,"Complete"] = "Yes"
        print(f"{v} has been marked complete.")
    else:
        print("The task is not in the list")
        retry = input("You want to try another task: 'Y' to retry, any else character to return to menu:")
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
            if task:                        # check if the input is not empty
                add_task(task)
            else:                           # validate if new task is empty
                print("Invalid input. Task cannot be empty.\n")
        elif request == "2":
            remove_task()
        elif request == "3":
            print("The existing tasks are the following: ")
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
                    save_tasks()            # save changes if user chooses
                elif save_user != 'n':
                    print("Invalid choice. Exiting without saving.")
            print("Exiting the application. Goodbye!")
            break
        else:                               # validate wrong inputs
            print("Invalid choice. Please try again.\n")

# call the main menu
main()