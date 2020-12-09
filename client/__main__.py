import argparse
from tree.node import Node
from tree.treeMechanics import search_tree
from utils.utils import get_doc_from_input
from utils.json_tools import encode, decode


def main():

    root = decode("dataset/operating_data.json")
    current_node = root
    temp_node=root
    while current_node:
        print(current_node)
        user_input = get_doc_from_input(">")
        temp_node = current_node
        if current_node.check_for_solutions(user_input) is not None:
            return
        else:
            current_node = current_node.search_branch(user_input)
            if not current_node:
                current_node = temp_node.search_other_branches(user_input)
                if not current_node:
                    add_solution_to_tree(root)


    encode(root, "dataset/operating_data.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)



# main function to start adding solution
def add_solution_to_tree(root:Node):
    print("Sorry I can't help you, Can you tell me how to solve it?")
    user_solution = get_doc_from_input("*your solution** >")
    root_children_sorted = get_all_root_children_listed_by_similarity(root, user_solution)
    choosen_node = search_good_node_to_add_solution_to_in_branch(root_children_sorted[0], 0.8, user_solution)

    if choosen_node is Node:
        choosen_node.add_solution(user_solution)
        print("dodalem")
        print(choosen_node)
    elif choosen_node is None:
        index = 1
        while choosen_node is None:
            if index >= len(root_children_sorted):
                choosen_node = ask_for_question(root, user_solution)
                break
            choosen_node = search_good_node_to_add_solution_to_in_branch(root_children_sorted[index], 0.8, user_solution)
            index += 1
        choosen_node.add_solution(user_solution)
        print("dodalem solution")
        print(choosen_node)


def get_all_root_children_listed_by_similarity(root: Node, user_solution):
    list = root.getChildren()
    listOfSimilarityValue = []
    for i in range(0, len(list)):
        result = list[i].getData().similarityValue(user_solution)
        listOfSimilarityValue.append(result)
    dictionary = nodes_and_similarity_value_lists_to_dictionary(listOfSimilarityValue, list)
    sort_orders = sorted(dictionary.items(), key=lambda x: x[0])
    dictlist = []
    for element in sort_orders:
        temp = element[1]
        dictlist.append(temp)
    return dictlist


# function which returns best node match to gotten solution or null if in branch there is none matching treshold
def search_good_node_to_add_solution_to_in_branch(branch_node: Node, treshold: float, user_solution):
    return search_tree(branch_node, user_solution)


def nodes_and_similarity_value_lists_to_dictionary(test_keys, test_values):
    return {test_keys[i]: test_values[i] for i in range(len(test_keys))}


def ask_for_question(root: Node):
    print("Sorry I can't find a question suited to add your solution, Can you tell me how should I ask for this problem?")
    user_question = get_doc_from_input("*your solution** >")
    choosen_node = search_tree(root, user_question)
    if(choosen_node is None):
        choosen_node = root
    choosen_node.addChild(user_question)
    children = choosen_node.getChildren()
    addedquestionnode = None
    for child in children:
        if child.getChildren() == None:
            addedquestionnode = child
            break
    return addedquestionnode
main()