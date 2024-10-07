import unittest
from task import Task
from task_storage import save_tasks, load_tasks


class TestTaskManagerApp(unittest.TestCase):
    
    def setUp(self):
        #This method will run before each test
        self.task = Task(title="Test Task", description="A simple test task", due_date="2024-10-10", category="Test")
        
        
    def test_task_creation(self):
        #Test if a task is created correctly
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "A simple test task")
        self.assertEqual(self.task.due_date, "2024-10-10")
        self.assertEqual(self.task.category, "Test")
        self.assertFalse(self.task.completed) #By default, the tasks should be incomplete
        
        
    
    def test_mark_completed(self):
        #Test if a task can be marked as complete
        self.task.mark_completed()
        self.assertTrue(self.task.completed)
        
        
    def test_task_repr(self):
        #Test the string representation of a task
        expected_repr = "Test Task [Incomplete, Due: 2024-10-10, Category: Test]"
        self.assertEqual(repr(self.task), expected_repr)
        
        #mark as complete and check again
        self.task.mark_completed()
        expected_repr_completed = "Test Task [Completed, Due: 2024-10-10, Category: Test]"
        self.assertEqual(repr(self.task), expected_repr_completed)
        
        
        
    def test_task_storage_save_load(self):
        #Test saving and loading tasks from the file
        tasks = [self.task] #List of tasks
        save_tasks(tasks) #Save the task to file
        
        loaded_tasks = load_tasks() #Load the tasks back from the file
        self.assertEqual(len(loaded_tasks), 1) #There should be one task in the file
        loaded_task = loaded_tasks[0]
        
        
        #Check that the loaded task matches the original task
        self.assertEqual(loaded_task.title, self.task.title)
        self.assertEqual(loaded_task.description, self.task.description)
        self.assertEqual(loaded_task.due_date, self.task.due_date)
        self.assertEqual(loaded_task.category, self.task.category)
        self.assertFalse(loaded_task.completed) #Ensure it's still incomplete
        
        
    def test_task_storage_mark_complete(self):
        #Test saving/loading tasks with completed status
        self.task.mark_completed()
        save_tasks([self.task]) #Save the task to file
        
        loaded_tasks = load_tasks() #Load the tasks back from the file
        self.assertTrue(loaded_tasks[0].completed) #Task should be marked complete now
        

if __name__ == '__main__':
    unittest.main()