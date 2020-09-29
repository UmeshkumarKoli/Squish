def step(context):
    action.startApplication()
    obj=waitForObject(names.mainWindow_MainWindow)
    listAll = getChildrenOfType(obj, "BasicFrame")
    for child in listAll:
        snooze(2)
        action.mouseOnClick(child)
        

def getChildrenOfType(parent, typename, depth=1000):
    children = []
    for child in object.children(parent):
        if className(child) == typename:
            children.append(child)
        if depth:
            children.extend(getChildrenOfType(child, typename, depth - 1))
    return children