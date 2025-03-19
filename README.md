# To-Do List Application

## Contributors
- Maria Jose Teran
- Sebastian Melendez

## Overview
This project consists of two versions of a To-Do List application, each with different functionalities:

1. **To-Do List Application 1 (TDL1)**: A simple version that allows users to add, remove, and view tasks.
2. **To-Do List Application 2 (TDL2)**: An advanced version that includes task prioritization, deadlines, task suggestions, and file-saving features.

## Features
### TDL1 (Basic Version)
- **Add tasks** to the to-do list.
- **Remove tasks** from the list.
- **View tasks** currently in the list.
- **Mark tasks as completed**.
- **Save and load tasks** from a file.

### TDL2 (Advanced Version)
- **All features from TDL1**, plus:
- **Set deadlines** for tasks.
- **Assign priority levels** (high, medium, low).
- **View tasks sorted by priority and deadline**.
- **Receive task suggestions** based on urgency and priority.

## How to Use

### 1. Clone the Repository
```sh
git clone https://github.com/mjteran/To_Do_List_app.git
```

### 2. Navigate to the Project Directory
```sh
cd To_Do_List_app
```

### 3. Install Dependencies (Required for TDL2)
Ensure you have Python installed, then install the necessary package:
```sh
pip install pandas
```

### 4. Run the Application
You can choose either version to run:
- **For the basic version (TDL1):**
  ```sh
  TDL1.py
  ```
- **For the advanced version (TDL2):**
  ```sh
  TDL2.py
  ```

### 5. Application Menu Options
Upon running the application, you will see a menu with the following options:

#### TDL1 Menu:
1. Add Task
2. Remove Task
3. View Tasks
4. Mark Task as Complete
5. Load Tasks from File
6. Save Tasks to File
7. Exit

#### TDL2 Menu (Includes Additional Features):
1. Add Task (with deadline and priority)
2. Remove Task
3. View Tasks (sorted by priority and deadline)
4. Mark Task as Complete
5. Suggest Tasks (based on urgency and priority)
6. Load Tasks from File
7. Save Tasks to File
8. Exit

### 6. File Handling
- Tasks can be **saved** and **loaded** from a file named `tasks.txt`.

## Notes
- Both applications are command-line-based and require user input for managing tasks.
