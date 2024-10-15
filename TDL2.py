# To-Do List Application 2 - Group 7
#   - Sebastian
#   - Maria Jose

# Objective:
# Create a comprehensive to-do list application that allows users to add, remove, view, prioritize tasks, and set
# deadlines. Additionally, implement a feature to suggest tasks based on priority and approaching deadlines using
# basic AI logic.

# Advanced to-do list application coding:

# import the main libraries
from datetime import datetime
import pandas as pd

# global variables:
task_df = pd.DataFrame(columns=['Task','Priority', 'Date', 'Priority_Value',"Complete"])
today_date = datetime.today().date()
changes_unsaved = False
# priorities:
p_value = {'high': 1, 'medium': 2, 'low': 3}

# functions:
# function to add tasks to the list:
def add_task(task):
    global changes_unsaved, p_value, task_df
    if task in task_df['Task'].values:                           # validate if task already exists
        print(f"'{task}' is already in the list. Duplicate tasks are not allowed.\n")
        return
    allow = ["high", "medium", "low"]
    while True:                                                 # determine if the priority is acceptable
        priority = input("Enter the priority (high,medium,low):").strip().lower()
        if priority in allow:
            break
        else:
            print("Not valid priority, please try again.")

    f = "%Y-%m-%d"                                              # date format
    while True:                                                 # determine if the date is acceptable
        day = input("Enter the deadline (YYYY-MM-DD):")
        try:
            date = datetime.date(datetime.strptime(day,f))
            if date < today_date:             # check if the date is before today
                print(f"Invalid date entered {date}. Deadline can't be in the past. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date entered. Please try again.")

    # add new task as a row
    new_task = {'Task':task,'Priority':priority, 'Date':date, 'Priority_Value':p_value[priority], 'Complete': "No"}
    task_df.loc[len(task_df)] = new_task  # append the new task as a row
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
    print()

def suggest_task():
    if task_df.empty:                                                   # if the list of tasks is empty
        print("The To-do List is empty.No suggestions.\n")
        return
    task_sug = task_df[task_df['Complete'] == 'No']                     # filter the tasks completed
    task_sug['Date'] = pd.to_datetime(task_df['Date'])                  # 'Date' to datetime for sorting
    task_sorted = task_sug.sort_values(by=['Priority_Value','Date'])    # sort by Priority values
    print("Good afternoon! Here are some tasks you might want to work on:")
    print(task_sorted[["Task",'Priority',"Date"]])
    print()

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
    if not task_df.items:  # if list of tasks is empty
        print("The To-do List is empty. No file saved.\n")
        return
    task_df['Date'] = pd.to_datetime(task_df['Date']).dt.strftime('%Y-%m-%d')
    task_df.to_csv(filename, index=False,header=False,sep=',')   # write tasks in the file
    print(f"Tasks saved to {filename}.\n")
    changes_unsaved = False

# function to load the task list from a file
def load_tasks(filename='tasks.txt'):                   # load the tasks file
    new_task = 0
    try:
        with open(filename, 'r') as file:               # read the tasks
            for line in file:                           # read each line of the file
                task = line.strip().strip("[]").split(",")                  # split the line into task's elements
                # verify the information from file
                if len(task) == 3:                      # if task has 3 elements (task, priority, date)
                    task_i, priority, date = task
                    status = "No"
                elif len(task) == 5:                    # if task has all elements
                    task_i, priority, date, prior_value, status = task
                else:                                   # if task is incomplete skip
                    continue
                # verify the priority is the required
                if priority in p_value:                 # if the priority is a valid number
                    prior_value = p_value[priority]
                else:
                    continue
                # verify a valid date
                try:
                    d = datetime.strptime(date.strip(), "%Y-%m-%d").date()  # format to date
                except ValueError:                      # if date is incorrect skip
                    continue
                # to assign line to task
                if task_i and task_i not in task_df['Task'].values and d >= today_date:  # avoid duplicates
                    task_df.loc[len(task_df)] = [task_i.strip(), priority.strip(), date.strip(), prior_value,
                                                status.strip()]  # append as list
                    new_task += 1                       # count new tasks
        if new_task > 0:
            print(f"{new_task} valid task(s) were loaded from {filename}.\n")
            return
        else:
            print("The file was read, but no tasks were loaded.\n")
    except FileNotFoundError:                           # error if file not found or not tasks
        print(f"File '{filename}' not found.\n")

# function to mark a task as completed
def mark_task():
    if not task_df:
        print("The To-do List is empty.")
        return
    task_c = input("Enter the complete task:").strip()
    if task_c in task_df["Task"].values:
        task_df.loc[task_df["Task"] == task_c,"Complete"] = "Yes"
        print(f"{task_c} has been marked complete.")
    else:
        print("The task is not in the list")
        retry = input("You want to try another task: 'Y' to retry, any else character to return to menu:")
        if retry.lower() == 'y':
            mark_task()

def main():
    while True:
        print("Advanced To - Do List Application:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark complete task")
        print("5. Suggest tasks")
        print("6. Load Tasks list from a File")
        print("7. Save Tasks to a File")
        print("8. Exit")
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
            suggest_task()
        elif request == "6":
            load_tasks()
        elif request == "7":
            save_tasks()
        elif request == "8":
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