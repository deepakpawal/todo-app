#from functions import get_todos, write_todos
import functions as f
import time

print(f'The time is {time.strftime('%b %d, %Y %H:%M:%S')}')

while True:
     user_action=input("Type add, show, edit, complete, exit:")
     user_action=user_action.strip()

     if user_action.startswith("add"):
          todo=user_action[4:]+ "\n"

          todos=f.get_todos()

          todos.append(todo)

          f.write_todos(todos)

     elif user_action.startswith("show"):
         todos=f.get_todos()

    #can be done via list comprehension
         for index,item in enumerate(todos):
             item=item.strip('\n')
             print(f'{index+1}.{item.title()}')

     elif user_action.startswith("edit"):
         try:
             todos=f.get_todos()

             x=user_action[5:]
             x=int(x)-1

             new=input(f"Enter new todo instead of : {todos[x].strip("\n")} :")
             todos[x]=new + '\n'

             f.write_todos(todos)
             print("Edited successfully")
         except ValueError:
             print("Your command is not valid")
             continue


     elif 'complete' in user_action:
         try:
             complete=user_action[9:]
             todos=f.get_todos()
             complete=int(complete)-1
             print(f'"{todos.pop(complete).strip('\n').title()}" is completed and removed')
             f.write_todos(todos)

         except IndexError:
             print("There is no item with that error")
             continue


     elif "exit" in user_action:
         break
     else:
         print("Invalid command entry")


print("Bye")