class Task:
    def __init__(self, id, desc, status=["todo", "In progress", "done"], created_at, updated_at):
        self.id = id
        self.desc = desc
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at