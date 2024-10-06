import json
from task import Task

TASKS_FILE = 'tasks.json'

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json_tasks = [task.__dict__ for task in tasks]
        json.dump(json_tasks, f, indent=4)


def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks_data = json.load(f)
            return [Task(**task) for task in tasks_data]
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exit or is empty/corrupted, return an empty list. "Error handling"
        return []
    

def delete_task(tasks, title):
    return [task for task in tasks if task.title != title]