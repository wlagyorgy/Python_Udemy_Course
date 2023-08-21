# from functions import write_todos
# from functions import get_todos as gett

import functions
import time

text = """
Multi
line
string
"""
# print(text)

now = time.strftime("%Y. %b %d. %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] -- list comprehensions
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}. {item}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1
            todos = functions.get_todos()

            new_todo = input("New ToDo: ")
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(filepath='../bonus/todos.txt', todos_local=todos)

            message = f"Todo - {todo_to_remove} - was completed and removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("You have entered an unknown command")
print("Bye")
