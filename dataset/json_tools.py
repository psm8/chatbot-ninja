import json

from tree.node import Node


def encode() -> Node:
    with open("dataset/tree_data.json", "r") as f:
        test = f.read()
        test_json = json.loads(test)
        node = Node(test_json["question"], None, get_children(test_json["children"]))
    return node


def get_children(children:[]) -> [Node]:
    nodes = []
    for child in children:
        nodes.append(Node(child["question"], child["solutions"], get_children(child["children"])))

    return nodes


def decode(node: Node,):
    with open("dataset/tree_data2.json", "w") as f:
        test = json.dumps(node)
        f.write(test)


test = encode()
test2 = decode(test)