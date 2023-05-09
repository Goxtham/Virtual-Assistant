from neuralintents import GenericAssistant
import pandas_datareader as web
import sys


todos = ['Eat','Workout','Study','Sleep']

        
def todo_show():
    print("Your TODO list:")
    for todo in todos:
        print(todo)

def todo_add():
    todo = input("What TODO do you want to add: ")
    todos.append(todo)

def todo_remove():
    idx = int(input("Which TODO to remove (number): "))-1
    if idx<len(todos):
        print(f"Removing {todos[idx]}")
        todos.pop(idx)
    else:
        print("There is no TODO at this position")

def bye():
    print("Bye")
    sys.exit(0)
    
mappings = {'todoshow': todo_show,
            'todoadd': todo_add,
            'todoremove':todo_remove,
            'goodbye':bye}
    
assistant = GenericAssistant('intents.json', mappings)

assistant.train_model()
assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        assistant.request(message)
        