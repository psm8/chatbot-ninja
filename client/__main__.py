import argparse
from utils.utils import get_doc_from_input
from utils.json_tools import encode, decode


def main():

    root = decode("dataset/operating_data.json")
    current_node = root
    temp_node = root
    nth_best = 0
    old_user_input = None

    while current_node:
        print(current_node)
        user_input = get_doc_from_input(">")
        temp_node = current_node
        if current_node.check_for_solutions(user_input) is not None:
            return
        else:
            temp_node, current_node, nth_best, old_user_input = current_node.search_branch(temp_node, user_input, old_user_input, nth_best)
            if not current_node:
                current_node = temp_node.search_other_branches(old_user_input)

                if not current_node:
                    temp_node.add_solution_to_tree(old_user_input)

    encode(root, "dataset/operating_data.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")


main()
