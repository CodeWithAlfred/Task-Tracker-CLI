def create():
    return "Task created"

def update():
    return "Task updated"

def delete():
    return "Task deleted"

def list_done():
    return "All your done tasks are"

def list_in_progress():
    return "Your tasks in progress:"

def list_todo():
    return "Your todo list:"

operations = {
    "create task": create, 
    "update  task": update,
    "delete task": delete,
    "list done": list_done,
    "list in-progress": list_in_progress,
    "list todo": list_todo
}

def u_input_handler():
    user_input = input("Enter operation: ")

    if user_input in operations:
        print(operations[user_input]())
    else:
        print("Sorry, command not found")
        u_input_handler()

u_input_handler()