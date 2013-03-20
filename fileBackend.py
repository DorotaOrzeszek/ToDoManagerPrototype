def generateID(todoList):
  maxID = 0
  for todoID in todoList.keys():
    if todoID > maxID:
      maxID = todoID
  nextID = maxID + 1
  return nextID

class Backend():
  def __init__ (self, filePath):
    self.filePath = filePath
  
# todoFile contains a dictionary     
  def _readTodoFile(self):
    todoFile = open(self.filePath,"r")
    todoList = eval(todoFile.read())
    todoFile.close()
    return todoList
  
  def showTodo(self, todoID):
    todoToShow = self._readTodoFile()[todoID]
    return todoToShow
  
  def showAllTodos(self):
    allTodos = self._readTodoFile()
    todosToShow = {}
    for todoID in allTodos.keys():
      shortTodoRecord = {todoID: {'name': allTodos[todoID]['name'],'priority': allTodos[todoID]['priority']}}
      todosToShow.update(shortTodoRecord)
    return todosToShow
        
  def removeTodo(self, todoID):
    todoList = self._readTodoFile()
    todoFile = open(self.filePath,"w")
    try:
      del todoList[todoID]
      todoFile.write(repr(todoList))   
    except KeyError:
      print 'No such todo'
    # updating the todoFile
    todoFile.close()
  
  def addTodo(self, name, priority):
    todoList = self._readTodoFile()
    todoFile = open(self.filePath,"w")
    newTodoID = generateID(todoList)
    todoList[newTodoID] = {'name': name, 'priority': priority}
    todoFile.write(repr(todoList))
    todoFile.close()
    return newTodoID
  
  def modifyTodo(self,todoID,changes):
    # changes is a dictionary:
    # {propertyName: newValue, ... }
    todoList = self._readTodoFile()
    todoFile = open(self.filePath,"w")
    todoToModify = todoList[todoID]
    for propertyName in changes:
      newValue = changes[propertyName]
      if newValue == None or "":
        del todoToModify[propertyName]
      else:
        todoToModify[propertyName] = newValue
    todoFile.write(repr(todoList))
    todoFile.close()
