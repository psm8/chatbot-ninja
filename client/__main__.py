import argparse
from tree.node import Node
from tree.treeMechanics import search_tree
from sentence.spaCyTreeNode import SpaCyTreeNode
import pickle
from utils.utils import ask_if_it_helped, get_doc_from_input

def init_tree():
    root = Node("How can I help You?")

    child1 = Node("So the problem is cornering. Can you add more details?")
    child2 = Node("So your car struggle onn straights. Can you add more details?")
    child3 = Node("So you got problems on different surface or in rain. Can you add more details?")
    child4 = Node("You can't get the feel of brakes. Can you add more detail?")

    root.addChild(child1)
    root.addChild(child2)
    root.addChild(child3)
    root.addChild(child4)

    child11 = Node("So you are understeering. Does this happen on fast or slow corners?")
    child12 = Node("Oversteer")
    child21 = Node("Top Speed")
    child31 = Node("Bumps and curbs")
    child41 = Node("Tyre Lockup")

    child1.addChild(child11)
    child1.addChild(child12)
    child2.addChild(child21)
    child3.addChild(child31)
    child4.addChild(child41)

    pickle.dump(root, open("temp_save.p", "wb"))

def main():

    while True:
        #init_tree()
        root = pickle.load(open("temp_save.p", "rb"))
        current_node = root
        temp_node=root
        helped = False
        while current_node:
            print(current_node)
            user_input = get_doc_from_input(">")
            temp_node = current_node
            if current_node.check_for_solutions(user_input) is not None:
                if ask_if_it_helped():
                    helped = True
                    break
            current_node = current_node.search_branch(user_input)
            if not current_node:
                current_node = temp_node.search_other_branches(user_input)


        if not helped:
            print("Sorry I can't help you, Can you tell me how to solve it?")
            user_solution = input("*your solution** >")
            temp_node.generate_question(user_solution)
            pickle.dump(root, open("temp_save.p", "wb"))
        else:
            print("You're welcome")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)

main()
