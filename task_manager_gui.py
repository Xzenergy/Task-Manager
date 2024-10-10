import tkinter as tk
from tkinter import messagebox, ttk
from task import Task
from task_storage import save_tasks, load_tasks


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XZenTask")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        
        #Load tasks
        self.tasks = load_tasks()
        

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=6, background="#4CAF50", foreground="white", borderwidth=0, relief="flat")
        style.map("TButton", background=[("active", "#45a049")])#Button color on hover


        
        #Main UI components

        #Title Label
        self.title_label = tk.Label(root, text="XZenTask", font=("Helvetica", 20, "bold", "italic"), bg="#f0f0f0", fg="#333333")
        self.title_label.pack(pady=20)
        
        
        #Dropdown for sorting tasks
        self.sort_by_var = tk.StringVar(value="Sort by")
        sort_options = ["Due Date", "Completion Status"]
        self.sort_by_dropdown = ttk.Combobox(root, textvariable=self.sort_by_var, values=sort_options, state="readonly")
        self.sort_by_dropdown.pack(pady=10)
        
        #Buttons with custom styles
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="green", fg="white", font=("Arial", 12))
        self.add_task_button.pack(pady=5)
        
        
        self.list_tasks_button = tk.Button(root, text="List Tasks", command=self.list_tasks, bg="blue", fg="white", font=("Arial", 12))
        self.list_tasks_button.pack(pady=5)
        
        
        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task, bg="orange", fg="black", font=("Arial", 12))
        self.complete_task_button.pack(pady=5)
        
        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg="red", fg="white", font=("Arial", 12))
        self.delete_task_button.pack(pady=5)
        


    def add_task(self):
        #Create a pop-up window to add tasks
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Task")
        add_window.geometry("300x300")
        add_window.coonfigure(bg="#ffffff") #White background
    
    
        #Labels and Entries
        tk.Label(add_window, text="Title:", font=("Arial", 10), bg="#ffffff").pack(pady=5)
        title_entry = tk.Entry(add_window)
        title_entry.pack()
    
    
        tk.Label(add_window, text="Description:", font=("Arial", 10), bg="#ffffff").pack(pady=5)
        description_entry = tk.Entry(add_window)
        description_entry.pack()
    
    
        tk.Label(add_window, text="Due Date (YYYY-MM-DD):", font=("Arial", 10), bg="#ffffff").pack(pady=5)
        due_date_entry = tk.Entry(add_window)
        due_date_entry.pack()
    
    
        tk.Label(add_window, text="Category:", font=("Arial", 10), bg="#ffffff").pack(pady=5)
        category_entry = tk.Entry(add_window)
        category_entry.pack()
    
    
    
        def save_new_task():
            #Create a task from the form inputs
            title = title_entry.get()
            description = description_entry.get()
            due_date = due_date_entry.get() if due_date_entry.get() else None
            category = category_entry.get() if category_entry.get() else None
    
            if not title:
                messagebox.showerror("Error", "Title is required!")
                return
    
    
    
            new_task = Task(title, description, due_date, category)
            self.tasks.append(new_task)
            save_tasks(self.tasks)
            messagebox.showinfo("Success", "Task added successfully!")
            add_window.destroy()
        
        #Add the save button
        save_button = tk.Button(add_window, text="Save Task", command=save_new_task)
        save_button.pack(pady=10)
    
    
    
    def list_tasks(self):
        sort_option = self.sort_by_var.get()
        if sort_option == "Due Date":
            self.tasks.sort(key=lambda task: (task.due_date is None, task.due_date))
        elif sort_option == "Completion Status":
            self.tasks.sort(key=lambda task: task.completed)
            
        #Create a new window to display the tasks
        list_window = tk.Toplevel(self.root)
        list_window.title("Task List")
    
        if not self.tasks:
            tk.Label(list_window, text="No tasks available at the moment.").pack(pady=10)
            return
    
        for i, task in enumerate(self.tasks, start=1):
            task_label = tk.Label(list_window, text=f"{i}. {task}")
            task_label.pack()  



    def complete_task(self):
        #Create a pop-up to mark a task as complete
        complete_window = tk.Toplevel(self.root)
        complete_window.title("Complete Task")
     
     
        tk.Label(complete_window, text="Enter Task Title to Complete:").pack(pady=5)
        task_title_entry = tk.Entry(complete_window)
        task_title_entry.pack()
     
     
        def complete_selected_task():
         task_title = task_title_entry.get()
         
         
         for task in self.tasks:
             if task.title == task_title:
                 task.mark_completed()
                 save_tasks(self.tasks)
                 messagebox.showinfo("Success", f"Task '{task_title}' marked as complete!")
                 complete_window.destroy()
                 return
        
         messagebox.showerror("Error", f"No task found with title '{task_title}'.") 
        
        
        #Complete button
        complete_button = tk.Button(complete_window, text="Complete Task", command=complete_selected_task)
        complete_button.pack(pady=10)
    


    def delete_task(self):
        #Create a pop-up to delete a task
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Task")
    
    
        tk.Label(delete_window, text="Enter Task Title you would like to Delete:").pack(pady=5)
        task_title_entry = tk.Entry(delete_window)
        task_title_entry.pack()
    
    
        def delete_selected_task():
            task_title = task_title_entry.get()
            original_count = len(self.tasks)
            self.tasks = [task for task in self.tasks if task.title != task_title]
        
            if len(self.tasks) < original_count:
                save_tasks(self.tasks)
                messagebox.showinfo("Success", f"Task '{task_title}' deleted!")
                delete_window.destroy()
            
            else:
                messagebox.showerror("Error", f"No task found with title '{task_title}'.")
            
            
        #Delete button
        delete_button = tk.Button(delete_window, text="Delete Task", command=delete_selected_task)
        delete_button.pack(pady=10)
    
    
    def edit_task(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")
        
        tk.Label(edit_window, text="Enter Task Title to Edit:").pack(pady=5)
        task_title_entry = tk.Entry(edit_window)
        task_title_entry.pack()
        
        def load_task_for_edit():
            task_title = task_title_entry.get()
            
            for task in self.tasks:
                if task.title == task_title:
                    title_var.set(task.title)
                    description_var.set(task.description)
                    due_date_var.set(task.due_date)
                    category_var.set(task.category)
                    return
            messagebox.showerror("Error", f"No task found with title '{task_title}'.")
            
            
        #Pre-populate fields with the tasks's current values
        title_var = tk.StringVar()
        description_var = tk.StringVar()
        due_date_var = tk.StringVar()
        category_var = tk.StringVar()

        tk.Label(edit_window, text="Title:").pack(pady=5)
        title_entry = tk.Entry(edit_window, textvariable=title_var)
        title_entry.pack()

        tk.Label(edit_window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(edit_window, textvariable=description_var)
        description_entry.pack()

        tk.Label(edit_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
        due_date_entry = tk.Entry(edit_window, textvariable=due_date_var)
        due_date_entry.pack()

        tk.Label(edit_window, text="Category:").pack(pady=5)
        category_entry = tk.Entry(edit_window, textvariable=category_var)
        category_entry.pack()



        def save_edited_task():
            task_title = task_title_entry.get()
            for task in self.tasks:
                if task.title == task_title:
                    task.title = title_var.get()
                    task.description = description_var.get()
                    task.due_date = due_date_var.get()
                    task.category = category_var.get()
                    save_tasks(self.tasks)
                    messagebox.showinfo("Success", f"Task '{task_title}' updated!")
                    edit_window.destroy()
                    return
            messagebox.showerror("error", f"No task found with title '{task_title}'.")
            
        
        
        #Buttons for loading task and saving edited task
        load_task_button = tk.Button(edit_window, text="Load Task", command=load_task_for_edit)
        load_task_button.pack(pady=5)
        
        save_button = tk.Button(edit_window, text="Save task", command=save_edited_task)
        save_button.pack(pady=10)
     
        
        
        
#Main Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
 
    
        