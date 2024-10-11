task_l = []
#add
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
        else:
            return main()

def main():
    view_task()