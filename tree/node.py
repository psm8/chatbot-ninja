from sentence.spaCyTreeNode import SpaCyTreeNode
from preprocess import preprocess
from utils.utils import ask_if_it_helped
from utils.utils import get_doc_from_input

class Node:

    def __init__(self, data, answer, solutions=None, children=None):

        self.data = SpaCyTreeNode(preprocess.preprocess(data), preprocess.preprocess(answer))
        self.parent = None
        self.children = []
        self.level = 0
        self.base_boarder = 0.4
        if solutions is not None:
            for solution in solutions:
                self.data.add_solution(solution[0], solution[1])
        if children is not None:
            for child in children:
                self.addChild(child)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data
        return False

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    # jak to dziala skoro to jest kopia xd przypisanie best_match powinno nie dzialac
    def getChildren(self):
        return self.children.copy()

    def getParent(self):
        return self.parent

    def getLevel(self):
        return self.level

    def addChild(self, child):
        self.children.append(child)
        child.parent = self
        child.level = self.level + 1

    def search_branch(self, data):
        similarity = self.base_boarder
        best_match = None
        children_list = self.getChildren()
        for child in children_list:
            result = child.getData().similarityValue(data)
            if result > similarity:
                best_match = child
                similarity = result
        print(similarity)
        return best_match

    def search_other_branches(self, data):
        similarity = self.base_boarder
        best_match = None
        current_node = self

        while current_node.getParent():
            current_node = current_node.getParent()

        children_list = current_node.getChildren()

        while children_list[0].getLevel() <= self.getLevel():
            result = children_list[0].getData().similarityValue(data)
            if result > similarity and not self == children_list[0]:
                best_match = children_list[0]
                similarity = result
            current_node = children_list[0]
            current_node_children = current_node.getChildren()

            # for i in list:
            #     print(i)

            children_list.pop(0)
            if len(current_node_children) > 0:
                for i in range(0, len(current_node_children)):
                    children_list.append(current_node_children[i])
            if len(children_list) == 0:
                break
        #     print("\n*** one iter of while ***\n")
        # print("\n*** one method called ***\n")
        print(similarity)
        return best_match

    # Do zmiany zeby od razu tu leciał check czy rozwiazanie pasuje
    def add_solution(self, answer, solution):
        self.data.add_solution(answer, solution)

    #TODO zamienic na generacje z modelu
    def generate_question(self, user_answer, user_solution, new_question, typical_answer):
        new_child = Node(new_question.text, typical_answer.text)
        self.addChild(new_child)
        new_child.add_solution(user_answer, user_solution)

    def check_for_solutions(self, data):
        solutions = self.getData().pick_solution(data)
        if solutions is None:
            return None
        for solution in solutions:
            if data.similarity(solution) > self.base_boarder:
                if ask_if_it_helped(solution):
                    return solution[1].text
        return None

    def get_root(self):
        current_node = self
        while current_node.getParent():
            current_node = current_node.getParent()
        return current_node

    def toJSON(self):
        dict = {
            "question": self.data.doc.text,
            "typical_answer": self.data.typical_answer.text,
            "solutions": [[x[0].text, x[1].text] for x in self.data.solutions],
            "children": [x for x in self.children]
        }
        return dict

    # main function to start adding solution
    def add_solution_to_tree(self, answer_for_last_question):
        print("Sorry I can't help you, Can you tell me how to solve it?")
        user_solution = get_doc_from_input("*Please enter your solution** >")
        user_question = get_doc_from_input(
            "*Please enter your question which you would like to hear from me for this problem** >")
        user_answer = get_doc_from_input("*Please enter your answer for your question** >")
        root_children_sorted = self.get_root().get_all_root_children_listed_by_similarity(user_question)

        choosen_node = None
        index = 0
        while choosen_node is None:
            if index >= len(root_children_sorted):
                choosen_node = self.get_root()
                break
            choosen_node = root_children_sorted[index].search_good_node_to_add_solution_to_in_branch(0.8,
                                                                         user_question)
            index += 1
        if self == choosen_node:
            choosen_node.generate_question(user_answer, user_solution, user_question, answer_for_last_question)
        else:
            print(choosen_node)
            answer_for_last_question = get_doc_from_input("*Please enter your answer for the question** >")
            choosen_node.generate_question(user_answer, user_solution, user_question, answer_for_last_question)
        print("dodalem solution")
        print(choosen_node)

    def get_all_root_children_listed_by_similarity(self, user_question):
        root = self.get_root()
        list = root.getChildren()
        listOfSimilarityValue = []
        for i in range(0, len(list)):
            result = list[i].getData().similarityValueByQuestion(user_question)
            listOfSimilarityValue.append(result)
        dictionary = self.nodes_and_similarity_value_lists_to_dictionary(listOfSimilarityValue, list)
        sort_orders = sorted(dictionary.items(), key=lambda x: x[0])
        dictlist = []
        for element in sort_orders:
            temp = element[1]
            dictlist.append(temp)
        return dictlist

    # function which returns best node match to gotten solution or null if in branch there is none matching treshold
    def search_good_node_to_add_solution_to_in_branch(self, treshold: float, user_question):
        return self.search_tree(treshold, user_question)

    def nodes_and_similarity_value_lists_to_dictionary(self, test_keys, test_values):
        return {test_keys[i]: test_values[i] for i in range(len(test_keys))}

    def search_tree(self, similarity, data):
        best_match = None
        children_list = self.getChildren()
        while len(children_list) > 0:
            result = children_list[0].getData().similarityValue(data)
            if result > similarity:
                best_match = children_list[0]
                similarity = result
            current_node = children_list[0]
            current_node_children = current_node.getChildren()
            children_list.pop(0)
            if len(current_node_children) > 0:
                for i in range(0, len(current_node_children)):
                    children_list.insert(0, current_node_children[i])

        return best_match








