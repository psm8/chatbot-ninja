import json
from json import JSONEncoder

from tree.node import Node
from preprocess.preprocess import preprocess

def decode(address: str) -> Node:
    with open(address, "r") as f:
        json_in = json.loads(f.read())
        node = Node(json_in["question"], json_in["typical_answer"], None, get_children(json_in["children"]))
    return node


def get_children(children: []) -> [Node]:
    nodes = []
    for child in children:
        nodes.append(Node(child["question"], child["typical_answer"],
                          [[preprocess(x[0]), preprocess(x[1])] for x in child["solutions"]],
                          get_children(child["children"])))

    return nodes


def encode(node: Node, address: str):
    with open(address, "w") as f:
        json_out = json.dumps(node, cls=DefaultEncoder, indent=2)
        f.write(json_out)


class DefaultEncoder(JSONEncoder):
    def default(self, o):
        try:
            return o.toJSON()
        except:
            return o.__dict__
