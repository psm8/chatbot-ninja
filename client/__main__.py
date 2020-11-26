import argparse
from tree.node import Node
from tree.treeMechanics import search_tree
from sentence.spaCyTreeNode import SpaCyTreeNode
import pickle

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


    #init_tree()
    root = pickle.load(open("temp_save.p", "rb"))
    current_node = root
    temp_node=root
    helped = False
    while current_node:
        print(current_node)
        user_input = input(">")
        temp_node = current_node
        if len(current_node.getData().solutions) > 0: # if len == 0 false and > similiarity
            print(current_node.getData().solutions[0].text)
            control_question = input("*Was it helpful?** (yes/no) >")
            if control_question == 'yes':
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

# main function to start adding solution
def add_solution_to_tree(root:SpaCyTreeNode):
    print("Sorry I can't help you, Can you tell me how to solve it?")
    user_solution = input("*your solution** >")
    # TODO generate doc
    best_branch_node = choose_best_branch(root, user_solution, 0)
    choosen_node = search_good_node_to_add_solution_to_in_branch(best_branch_node, 0.8, user_solution)
    ignore = 1
    while choosen_node is None:
        best_branch_node = choose_best_branch(root, user_solution, ignore)
        choosen_node = search_good_node_to_add_solution_to_in_branch(best_branch_node, 0.8, user_solution)
        ignore += ignore
    else:
        choosen_node.add_solution(user_solution)




# function which choose the best branch from root to start searching through
def choose_best_branch(root:SpaCyTreeNode, user_solution, how_many_first_ignore):
    return True

# function which returns best node match to gotten solution or null if in branch there is none matching treshold
def search_good_node_to_add_solution_to_in_branch(branch_node:SpaCyTreeNode, treshold:int, user_solution):
    return True
