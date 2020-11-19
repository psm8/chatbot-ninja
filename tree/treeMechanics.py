def search_tree(node, data):
    similarity = 0
    best_match = None
    list = node.getChildren()
    while len(list) > 0:
        if data.similarityValue(list[0].getData) > similarity:
            best_match = list[0]
        current_node = list[0]
        current_node_children = current_node.getChildren()
        list.pop(0)
        if len(current_node_children) > 0:
            for i in range (0, len(current_node_children)):
                list.insert(0, current_node_children[i])

    return best_match
