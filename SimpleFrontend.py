import fileBackend
# how do I use the constructor?
backend = fileBackend.Backend("todoFile.txt")

def printMainScreen():
  shortcuts = ["s", "S", "+", "-", "m", "x"]
  messages = ["show todo", "show all todos","add todo", "remove todo", "modify todo", "exit"]
  print "\n", "\t", "MAGIC TODO MANAGER", "\n"
  for i in range(6):
    print "\t" + shortcuts[i] + "\t" + messages[i]
  print

while True:
  printMainScreen()
  usersChoice = raw_input()
  
  if usersChoice == "x":
    print "\nExiting Magic Todo Manager\n"
    break
    
  elif usersChoice == "s":
    todoID = input("Show todo number (1-5)... ")
    todoToShow = backend.showTodo(todoID)
    print todoToShow
    
  elif usersChoice == "S":
    allTodos = backend.showAllTodos()
    for todo in allTodos:
      print todo, "==>", allTodos[todo]
    
  elif usersChoice == "+":
    name = raw_input("New todo's name... ")
    priority = input("New todo's priority... ")
    backend.addTodo(name, priority)
    print "Added new todo", name, priority
    
  elif usersChoice == "-":
    todoID = input("Reading todo number... ")
    backend.removeTodo(todoID)
    print "Removed todo", todoID
    
  elif usersChoice == "m":
    todoID = input("Reading todo number... ")
    changes = eval(raw_input("My changes... "))
    backend.modifyTodo(todoID, changes)
    print "Modified todo", todoID, "with", changes
  

