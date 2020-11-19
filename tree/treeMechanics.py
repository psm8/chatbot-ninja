def search_tree(node):
    list = node.getChildren()
    best_match = None
    while len(list) > 0:
        current_node = list[0]
        current_node_children = current_node.getChildren()
        list.pop(0)
        if len(current_node_children) > 0:
            for i in range (0, len(current_node_children)):
                list.insert(0, current_node_children[i])

    return best_match
