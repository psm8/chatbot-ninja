import argparse
from tree.node import Node
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
                    temp_node.add_solution_to_tree(user_input)


    encode(root, "dataset/operating_data.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)


main()