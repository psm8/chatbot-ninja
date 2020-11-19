import argparse
from tree.node import Node
from tree.treeMechanics import search_tree
from preprocess.preprocess import Preprocess
from sentence.spaCyTreeNode import SpaCyTreeNode
import pickle

def init_tree(preprocess):
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

    pickle.dump(root, open("temp_save.p", "wb"))

def main():

    preprocess = Preprocess()

    #init_tree(preprocess)
    root = pickle.load(open("temp_save.p", "rb"))
    current_node = root
    temp_node=root

    while current_node:
        print(current_node.getData().doc.text)
        preprocessed_input = preprocess.preprocess(input(">"))
        #print(SpaCyTreeNode(preprocessed_input).similarityValue(current_node.getData()))
        temp_node = current_node
        if current_node.check_solution(): # if len == 0 false and > similiarity
            if current_node.control_question():
                break

        #no
        current_node = current_node.search_branch(SpaCyTreeNode(preprocessed_input))
        if not current_node:
            current_node = temp_node.search_other_branches(SpaCyTreeNode(preprocessed_input))

    print("Sorry I can't help you, Can you tell me how to solve it?")
    user_solution = preprocess.preprocess(input("*your solution** >"))
    temp_node.generate_question(user_solution)

    pickle.dump(root, open("temp_save.p", "wb"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)

main()
