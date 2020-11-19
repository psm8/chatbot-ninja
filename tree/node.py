class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.level = 0

    def getData(self):
        return self.data

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getLevel(self):
        return self.level

    def addChild(self, child):
        self.children.append(child)
        child.parent = self
        child.level = self.level + 1

    def search_tree(self, data):
        similarity = 0
        best_match = None
        list = self.getChildren()
        while len(list) > 0:
            if data.similarityValue(list[0].getData) > similarity:
                best_match = list[0]
            current_node = list[0]
            current_node_children = current_node.getChildren()
            list.pop(0)
            if len(current_node_children) > 0:
                for i in range(0, len(current_node_children)):
                    list.insert(0, current_node_children[i])

        return best_match



