class Task:
    def __init__(self, id, desc, status=None, created_at, updated_at):
        self.id = id
        self.desc = desc
         self.status_values = ["todo", "In progress", "done"]
        if status is None: 
            self.status = self.status_value[0]
        elif status in status_values:
            self.status = status
        else:
            raise ValueError(f"Invalid  status description. Choose from: {', '.join(self.status_values)}")
       
        self.created_at = created_at
        self.updated_at = updated_at
