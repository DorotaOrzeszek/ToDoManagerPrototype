import pygtk
pygtk.require("2.0")
import gtk
import gobject
import fileBackend

backend = fileBackend.Backend("todoFile.txt")

def onButtonClicked(widget, data=None):
  display.set_text("You clicked " + data)
  
# Buttons

readTodoButton = gtk.Button("Show")
readTodoButton.connect("clicked",onButtonClicked,"Show")

readAllTodosButton = gtk.Button("Show all")
readAllTodosButton.connect("clicked",onButtonClicked,"Show all")

def showAddPopup(widget, data=None):
  todoNameLabel = gtk.Label("Todo")
  todoName = gtk.Entry()
  property1 = gtk.Label("Controls for property 1")
  property2 = gtk.Label("Controls for property 2")
  saveButton = gtk.Button("Save")
  discardButton = gtk.Button("Discard")
  popup = gtk.Window()
  popup.set_size_request(540,900)
  popup.set_border_width(30)
  popup.set_position(gtk.WIN_POS_CENTER)
  saveButton.connect("clicked",destroyThePopup,popup)
  discardButton.connect("clicked",destroyThePopup,popup)
  popuphbox2 = gtk.HBox()
  popuphbox2.pack_start(saveButton)
  popuphbox2.pack_start(discardButton)
  popuphbox3 = gtk.HBox()
  popuphbox3.pack_start(todoNameLabel)
  popuphbox3.pack_start(todoName)
  popupvbox1 = gtk.VBox()
  popupvbox1.pack_start(popuphbox3)
  popupvbox1.pack_start(property1)
  popupvbox1.pack_start(property2)
  popupvbox = gtk.VBox()
  popupvbox.pack_start(popupvbox1)
  popupvbox.pack_start(popuphbox2)
  popup.add(popupvbox)
  popup.show_all()
  return todoName.get_text()

addTodoButton = gtk.Button("Add")
addTodoButton.connect("clicked",showAddPopup,None)

def showRemovePopup(widget, data=None):
  warning = gtk.Label("Are you sure?")
  OKButton = gtk.Button("Yes")
  CancelButton = gtk.Button("No")
  popup = gtk.Window()
  popup.set_size_request(300,200)
  popup.set_border_width(30)
  popup.set_position(gtk.WIN_POS_CENTER)
  OKButton.connect("clicked",destroyThePopup,popup)
  CancelButton.connect("clicked",destroyThePopup,popup)
  popuphbox1 = gtk.HBox()
  popuphbox1.pack_start(OKButton)
  popuphbox1.pack_start(CancelButton)
  popupvbox = gtk.VBox()
  popupvbox.pack_start(warning)
  popupvbox.pack_start(popuphbox1)
  popup.add(popupvbox)
  popup.show_all()

removeTodoButton = gtk.Button("Remove")
removeTodoButton.connect("clicked",showRemovePopup,None)

# Modify todo screen

def destroyThePopup(widget, data):
  popup = data
  popup.destroy()

def showModifyPopup(widget, data=None):
  todoName = gtk.Label("Get name from checkboxed todo")
  property1 = gtk.Label("Controls for property 1")
  property2 = gtk.Label("Controls for property 2")
  saveButton = gtk.Button("Save")
  discardButton = gtk.Button("Discard")
  popup = gtk.Window()
  popup.set_size_request(540,900)
  popup.set_border_width(30)
  popup.set_position(gtk.WIN_POS_CENTER)
  saveButton.connect("clicked",lambda widget, data: popup.destroy(),None)
  discardButton.connect("clicked",destroyThePopup,popup)
  popuphbox2 = gtk.HBox()
  popuphbox2.pack_start(saveButton)
  popuphbox2.pack_start(discardButton)
  popupvbox1 = gtk.VBox()
  popupvbox1.pack_start(todoName)
  popupvbox1.pack_start(property1)
  popupvbox1.pack_start(property2)
  popupvbox = gtk.VBox()
  popupvbox.pack_start(popupvbox1)
  popupvbox.pack_start(popuphbox2)
  popup.add(popupvbox)
  popup.show_all()

modifyTodoButton = gtk.Button("Modify")
modifyTodoButton.connect("clicked",showModifyPopup,None)

def showExitPopup(widget, data=None):
  warning = gtk.Label("Don't do that!")
  sorryButton = gtk.Button("I'm sorry...")
  popup = gtk.Window()
  popup.set_size_request(300,200)
  popup.set_border_width(30)
  popup.set_position(gtk.WIN_POS_CENTER)
  sorryButton.connect("clicked",destroyThePopup,popup)
  popupvbox = gtk.VBox()
  popupvbox.pack_start(warning)
  popupvbox.pack_start(sorryButton)
  popup.add(popupvbox)
  popup.show_all()

exitButton = gtk.Button("Exit")
exitButton.connect("clicked",showExitPopup)


# Main display

display = gtk.Label("This displays your actions")

buttonsline1 = gtk.HBox()
buttonsline1.pack_start(addTodoButton)
buttonsline1.pack_start(modifyTodoButton)
buttonsline1.pack_start(removeTodoButton)
buttonsline2 = gtk.HBox()
buttonsline2.pack_start(exitButton)
buttons = gtk.VBox()
buttons.pack_start(buttonsline1)
buttons.pack_start(buttonsline2)

def createTreeView():
  listStore = gtk.ListStore(gobject.TYPE_INT, gobject.TYPE_STRING)
  treeView = gtk.TreeView(listStore)
  tvcolumn1 = gtk.TreeViewColumn("ID")
  tvcolumn2 = gtk.TreeViewColumn("Todo")
  treeView.append_column(tvcolumn1)
  treeView.append_column(tvcolumn2)
  renderer1 = gtk.CellRendererText()
  renderer2 = gtk.CellRendererText()
  tvcolumn1.pack_start(renderer1,True)
  tvcolumn2.pack_start(renderer2,True)
  tvcolumn1.add_attribute(renderer1,"text",0)
  tvcolumn2.add_attribute(renderer2,"text",1)
  return (treeView, listStore)

(treeView, listStore) = createTreeView()

def updateListStore():
  todoDict = backend.showAllTodos()
  for todoID in todoDict:
    listStore.append((todoID,todoDict[todoID]['name']))
    
updateListStore()
  
mainvbox = gtk.VBox()
mainvbox.pack_start(display)
mainvbox.pack_start(treeView)
mainvbox.pack_start(buttons)

mainScreen = gtk.Window()
mainScreen.set_title("Magic Todo Manager")
mainScreen.set_size_request(540,900)
mainScreen.set_border_width(30)
mainScreen.set_position(gtk.WIN_POS_CENTER)
mainScreen.connect("destroy", lambda wid: gtk.main_quit())
mainScreen.add(mainvbox)

mainScreen.show_all()
gtk.main()
