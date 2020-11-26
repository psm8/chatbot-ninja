import json

from tree.node import Node


def encode():
    with open("dataset/tree_data.json", "r") as f:
        test = f.read()
        test_json = json.loads(test)
        node = Node(test_json["question"])
    return 0

def get_children(children:[], ):

def decode(node: Node, json_adres: str):
    test = json.loads(json_adres)
    return 0


encode()