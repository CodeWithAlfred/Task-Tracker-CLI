import time

class Task:
    def __init__(self, id, desc, status=None):
        self.id = id
        self.desc = desc
        #self.created_at = created_at
        #self.updated_at = updated_at

        self.status_values = ["todo", "In progress", "done"]
        
        if status is None: 
            self.status = self.status_values[0]
        elif status in self.status_values:
            self.status = status
        else:
           #raise ValueError(f"Invalid  status description. Choose from: {', '.join(self.status_values)}")
           self.status = (f"Invalid  status description. Choose from: {' '.join(self.status_values)}")
          

    def show_status(self):
        return self.status

default_status = Task(1, "Buy Grocery", "do") 

print(default_status.show_status())