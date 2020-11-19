import argparse
from tree.node import Node
from tree.treeMechanics import search_tree, search_branch, search_other_branches
from preprocess.preprocess import Preprocess
from sentence.spaCyTreeNode import SpaCyTreeNode


def main():

    preprocess = Preprocess()



    data = SpaCyTreeNode(preprocess.preprocess("How can I help You?"))
    root = Node(SpaCyTreeNode(preprocess.preprocess("How can I help You?")))

    child1 = Node(SpaCyTreeNode(preprocess.preprocess("So the problem is cornering. Can you add more details?")))
    child2 = Node(SpaCyTreeNode(preprocess.preprocess("So your car struggle onn straights. Can you add more details?")))
    child3 = Node(SpaCyTreeNode(preprocess.preprocess("So you got problems on different surface or in rain. Can you add more details?")))
    child4 = Node(SpaCyTreeNode(preprocess.preprocess("You can't get the feel of brakes. Can you add more detail?")))

    root.addChild(child1)
    root.addChild(child2)
    root.addChild(child3)
    root.addChild(child4)

    child11 = Node(SpaCyTreeNode(preprocess.preprocess("So you are understeering. Does this happen on fast or slow corners?")))
    child12 = Node(SpaCyTreeNode(preprocess.preprocess("Oversteer")))
    child21 = Node(SpaCyTreeNode(preprocess.preprocess("Top Speed")))
    child31 = Node(SpaCyTreeNode(preprocess.preprocess("Bumps and curbs")))
    child41 = Node(SpaCyTreeNode(preprocess.preprocess("Tyre Lockup")))

    child1.addChild(child11)
    child1.addChild(child12)
    child2.addChild(child21)
    child3.addChild(child31)
    child4.addChild(child41)


    current_node = root

    while current_node:
        print(current_node.getData().doc.text)
        preprocessed_input = preprocess.preprocess(input(">"))
        print(SpaCyTreeNode(preprocessed_input).similarityValue(current_node.getData()))
        current_node = search_branch(current_node, SpaCyTreeNode(preprocessed_input))
        if not current_node:
            current_node = search_other_branches(root, SpaCyTreeNode(preprocessed_input))

    print("IDK")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)

main()
