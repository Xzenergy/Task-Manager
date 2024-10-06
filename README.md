# Task Management CLI Application

## Overview

The **Task Management CLI Application** is a simple, command-line tool that helps you manage and track tasks. It allows you to create tasks, assign due dates, categorize tasks, mark them as complete, and delete tasks. All tasks are saved to a JSON file (`tasks.json`) to ensure they persist across different runs of the application.

This project is ideal for intermediate Python developers looking to practice Object-Oriented Programming (OOP), file handling, and CLI-based user interaction.

## Features

- Add tasks with title, description, due date, and category.
- Mark tasks as complete.
- List all tasks with their status (completed or incomplete).
- Delete tasks.
- Save tasks to a file (`tasks.json`) to maintain persistence.
- Simple, intuitive command-line interface.

## Project Structure

```bash
task_manager/
│
├── task_manager.py    # Main CLI application
├── task.py            # Defines the Task class (OOP structure)
├── task_storage.py    # Handles reading/writing tasks to file
├── utils.py           # Utility functions for input validation
├── tasks.json         # File where tasks are saved (created at runtime)
└── README.md          # Project description and instructions


Requirements
Python 3.6 or higher

Setup 
Instructions
Clone this repository or download the project files.
Navigate to the project directory.
bash
Copy code
cd task_manager
Install any required dependencies (none at this point, but future enhancements may require libraries).
Run the task manager application:
bash
Copy code
python task_manager.py


Usage
After running the application, you will be presented with a menu with the following options:

markdown
Copy code
Task Manager

1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
1. Add a Task
You can add a task by selecting option 1. The application will prompt you for the following information:

Title: A short, descriptive name for the task.
Description: A more detailed explanation of the task.
Due Date: (Optional) You can specify a due date in YYYY-MM-DD format or leave it blank.
Category: (Optional) You can categorize the task, e.g., "Work", "Personal", etc.

Example:
yaml
Copy code
Enter task title: Buy groceries
Enter task description: Buy milk, eggs, and bread
Enter due date (YYYY-MM-DD) or leave blank: 2024-10-10
Enter category or leave blank: Personal
List: Tasks You can view all tasks, along with their completion status, by selecting option 2. For each task, you'll see its title, description, due date, category, and whether it is completed or not.


### Project Examples

Example output:

yaml
Copy code
1. Buy groceries [Incomplete, Due: 2024-10-10, Category: Personal]
2. Finish report [Completed, Due: 2024-10-05, Category: Work]
3. Complete a Task
To mark a task as complete, select option 3 and provide the title of the task you want to mark as done.

Example:

css
Copy code
Enter the title of the task to mark complete: Buy groceries
Task 'Buy groceries' marked as complete!
4. Delete a Task
To delete a task, select option 4 and enter the title of the task you want to remove.

Example:
arduino
Copy code
Enter the title of the task to delete: Finish report
Task 'Finish report' deleted!
5. Exit
Select option 5 to exit the application. All tasks will be saved to tasks.json, ensuring they persist for the next time you run the application.

Example
Here’s an example session of the Task Manager CLI in action:

yaml
Copy code
Task Manager

1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit

Choose an option: 1
Enter task title: Finish report
Enter task description: Complete the financial report
Enter due date (YYYY-MM-DD) or leave blank: 2024-10-05
Enter category or leave blank: Work
Task 'Finish report' added!

Choose an option: 2
1. Finish report [Incomplete, Due: 2024-10-05, Category: Work]

Choose an option: 3
Enter the title of the task to mark complete: Finish report
Task 'Finish report' marked as complete!

Choose an option: 2
1. Finish report [Completed, Due: 2024-10-05, Category: Work]

Choose an option: 5
Goodbye!


Known Issues
There is no undo option once a task is marked complete or deleted.
The JSON file (tasks.json) must not be manually edited, as improper formatting could break the application.

Future Enhancements
Add task sorting (e.g., by due date or completion status).
Provide support for editing tasks.
Add color-coded output for better readability in the CLI.
Implement task filtering by category or due date.

License
This project is licensed under the MIT License.