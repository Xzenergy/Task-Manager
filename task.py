from datetime import datetime


class Task:
    def __init__(self, title, description, due_date=None, category=None, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.category = category
        self.completed = completed


    def mark_completed(self):
        self. completed = True


    def __repr__(self):
        self.completed = True


    def __repr__(self):
        status = "Completed" if self.completed else "Incomplete"
        due = f", Due: {self.due_date}" if self.due_date else ""
        category = f", Category: {self.category}" if self. category else ""
        return f"{self.title} [{status}{due}{category}]" 
    
        