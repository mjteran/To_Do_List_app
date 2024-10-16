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
task_df = pd.DataFrame(columns=['Task','Priority', 'Deadline', 'Priority_Value','Complete'])
today_date = datetime.today().date()
changes_unsaved = False

# priorities:
p_value = {'high': 1, 'medium': 2, 'low': 3}

# functions:
# function to add tasks to the list:
def add_task(task):
    global changes_unsaved, p_value, task_df
    task_l = task_df['Task'].str.lower().str.strip()            # task from dataframe in lower and without spaces
    if task.lower().strip() in task_l.values:                   # verify duplicates
        print(f"'{task}' is already in the list. Duplicate tasks are not allowed.\n")
        return
    # to add priority
    allow = ['high', 'medium', 'low']                           # priority list
    while True:                                                 # determine if the priority is acceptable
        priority = input("Enter the priority (high,medium,low):").strip().lower()   # take priority input lower
        if priority in allow:
            break
        else:
            print("Not valid priority, please try again.")
    # to add deadline
    f = "%Y-%m-%d"                                              # date format
    while True:                                                 # determine if the date is acceptable
        day = input("Enter the deadline (YYYY-MM-DD):")
        try:
            date = datetime.strptime(day,f).date()
            if date < today_date:                               # check if the date is before today
                print(f"Invalid date entered {date}. Deadline can't be in the past. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date entered. Please try again.")
    # add new task as a row
    new_task = [task.strip(), priority, date, p_value[priority], "No"]
    task_df.loc[len(task_df)] = new_task        # append the new task as an extra row in dataframe
    changes_unsaved = True                      # flag to indicate changes
    print(f"'{task}' has been added to list.\n")

def view_task():
    if task_df.empty:                                                   # if the list of tasks is empty
        print("The To-do List is empty.\n")
        return
    task_df['Deadline'] = pd.to_datetime(task_df['Deadline'])           # 'Date' to datetime for sorting
    task_sorted = task_df.sort_values(by=['Deadline','Priority_Value'],ascending=[True,True])  # sort by Date & Priority
    print(task_sorted[['Task','Priority','Deadline','Complete']].to_string(justify='center'))
    print()

def suggest_task():
    if task_df.empty:                                                   # if the list of tasks is empty
        print("The To-do List is empty. No suggestions.\n")
        return
    task_sug = task_df[task_df['Complete'] == 'No']                     # filter the tasks completed
    if task_sug.empty:                                                  # if the list of tasks is empty after filter
        print("All tasks completed. No suggestions.\n")
        return
    else:
        task_sorted = task_sug.sort_values(by=['Deadline','Priority_Value'],ascending=[True,True])  # sort
        print("Good afternoon! Here are some tasks you might want to work on:")
        print(task_sorted[['Task','Priority','Deadline']].to_string(index=False, justify='center'))
        print()

# function to remove a task:
def remove_task():
    global changes_unsaved
    if task_df.empty:                                       # if list of tasks is empty and nothing to remove
        print("The To-do List is empty.\n")
        return
    # task input to remove
    task = input("Enter the task to remove: ").strip()      # remove extra spaces in the task
    if task == "":                                          # validate if task to remove is empty
        print("Invalid input. Task cannot be empty.\n")
        return
    # find rows where the task matches the user input
    matches = task_df[task_df['Task'].str.lower().str.strip() == task.lower()]
    if not matches.empty:                               # if matching tasks
        task_df.drop(matches.index, inplace=True)       # remove the matching rows
        changes_unsaved = True                          # flag that changes are unsaved
        print(f"'{task}' has been removed from the list.\n")
    else:                                               # if task is not in the list
        print(f"The task '{task}' is not in the list. Please ensure the task matches exactly.")
        retry = input("Would you like to try again? ('Y' to retry, any other character to return to the menu):")
        if retry.lower() == 'y':                        # to retry if failing
            remove_task()

# function to save the task list to a file
def save_tasks(filename='tasks.txt'):
    global changes_unsaved
    if task_df.empty:                                   # if list of tasks is empty
        print("The To-do List is empty. No file saved.\n")
        return
    task_df['Deadline'] = pd.to_datetime(task_df['Deadline']).dt.strftime('%Y-%m-%d')
    task_df.to_csv(filename, index=False, header=False, sep=",")   # write tasks in the file
    print(f"Tasks saved to {filename}.\n")
    changes_unsaved = False

# function to load the task list from a file
def load_tasks(filename='tasks.txt'):                   # load the tasks file
    new_task = 0
    global task_df
    try:
        with open(filename, 'r') as file:               # read the tasks
            for line in file:                           # read each line of the file
                task = line.strip().split(',')          # split the line into task's elements
                # verify the information from file
                if len(task) not in [3,4,5]:
                    print(f"Skipped. Invalid task format or information missing: {task}")
                    continue
                elif len(task) == 3:                      # if task has 3 elements (task, priority, date)
                    task_i, priority, date = task
                    prior_value = p_value[priority]
                    status = 'No'
                elif len(task) == 4:                      # if task has 4 elements (task, priority, date)
                    task_i, priority, date, prior_value = task
                    prior_value = int(prior_value)
                    status = 'No'
                else:                                       # if task has all elements
                    task_i, priority, date, prior_value, status = task
                # validate the priority
                if priority not in p_value:                 # if the priority is a valid number
                    print(f"Skipped. Invalid priority for task: {task}")
                    continue
                # validate the date
                try:                                        # validate the format
                    d = datetime.strptime(date.strip(), "%Y-%m-%d").date()  # format to date
                    if d < today_date:
                        print(f"Skipped past-due task: {task}")
                        continue
                except ValueError:                          # if date is incorrect skip
                    print(f"Skipped invalid date for task: {task}")
                    continue
                # assign to task
                if task_i.lower().strip() not in task_df['Task'].str.lower().str.strip().values:
                    task_df.loc[len(task_df)] = [task_i.strip(), priority.strip(), d, int(prior_value), status.strip()]
                    new_task += 1                           # count new tasks
        if new_task > 0:
            print(f"{new_task} valid task(s) were loaded from {filename}.\n")
            return
        else:
            print("The file was read, but no tasks were loaded.\n")
    except FileNotFoundError:                               # error if file not found or not tasks
        print(f"File '{filename}' not found.\n")

# function to mark a task as completed
def mark_task():
    global changes_unsaved
    if task_df.empty:                                   # is task list is empty return to menu
        print("The To-do List is empty.")
        return
    task_c = input("Enter the complete task: ").strip().lower() # task to be marked

    if task_c in task_df['Task'].str.lower().values:            # to find task in list
        i = task_df[task_df['Task'].str.lower() == task_c].index[0] # find row index
        if task_df.loc[i,'Complete'] == 'Yes':                  # verify is task completed
            print(f"'{task_c}' is already marked as complete.\n")
        else:                                                   # mark as complete
            task_df.loc[task_df['Task'].str.lower() == task_c, 'Complete'] = 'Yes'
            print(f"'{task_c}' has been marked complete.\n")
            changes_unsaved = True
    else:                                                       # task not in list
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