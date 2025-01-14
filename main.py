class Task:
    def __init__(self, id, desc, status=None, created_at, updated_at):
        self.id = id
        self.desc = desc
        self.status_values = ["todo", "In progress", "done"]
        self.created_at = created_at
        self.updated_at = updated_at
