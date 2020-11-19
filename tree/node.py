class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def getData(self):
        return self.data

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def addChild(self, child):
        self.children.append(child)
        child.parent = self


