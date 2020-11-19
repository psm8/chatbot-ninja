def search_tree(node, data):
    similarity = 0.2
    best_match = None
    list = node.getChildren()
    while len(list) > 0:
        if data.similarityValue(list[0].getData()) > similarity:
            best_match = list[0]
        current_node = list[0]
        current_node_children = current_node.getChildren()
        list.pop(0)
        if len(current_node_children) > 0:
            for i in range (0, len(current_node_children)):
                list.insert(0, current_node_children[i])

    return best_match

def search_branch(node, data):
    similarity = 0.2
    best_match = None
    list = node.getChildren()

    for i in range(0, len(list)):
        if (data.similarityValue(list[i].getData())) > similarity:
            best_match = list[i]
    return best_match

def search_other_branches(node, data):
    similarity = 0.2
    best_match = None
    current_node = node

    while current_node.getParent():
        current_node = current_node.getParent()

    list = current_node.getChildren()

    while list[0].getLevel() <= node.getLevel():
        if data.similarityValue(list[0].getData()) > similarity and not node.__eq__(list[0]):
            best_match = list[0]
        current_node = list[0]
        current_node_children = current_node.getChildren()
        list.pop(0)
        if len(current_node_children) > 0:
            for i in range (0, len(current_node_children)):
                list.insert(current_node_children[i])

    return best_match
