def search_tree(node, data):
    similarity = 0.2
    best_match = None
    children_list = node.getChildren()
    while len(children_list) > 0:
        result = children_list[0].getData().similarityValue(data)
        if result > similarity:
            best_match = children_list[0]
            similarity = result
        current_node = children_list[0]
        current_node_children = current_node.getChildren()
        children_list.pop(0)
        if len(current_node_children) > 0:
            for i in range (0, len(current_node_children)):
                children_list.insert(0, current_node_children[i])

    return best_match




