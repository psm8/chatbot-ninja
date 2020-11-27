from sentence.spaCyTreeNode import SpaCyTreeNode
from preprocess import preprocess
from utils.utils import ask_if_it_helped

class Node:

    def __init__(self, data, solutions=None, children=None):

        self.data = SpaCyTreeNode(preprocess.preprocess(data))
        self.parent = None
        self.children = []
        self.level = 0
        self.base_boarder = 0.2
        if solutions is not None:
            for solution in solutions:
                self.data.add_solution(solution)
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
    def add_solutions(self, solution):
        self.data.add_solution(solution)

    #TODO zamienic na generacje z modelu
    def generate_question(self, user_solution):
        new_question = self.data.generate_question(user_solution)
        new_child = Node(new_question.text)
        self.addChild(new_child)
        new_child.add_solutions(user_solution)

    def check_for_solutions(self, data):
        solutions = self.getData().pick_solution(data)
        if solutions is None:
            return None
        for solution in solutions:
            if data.similarity(solution) > self.base_boarder:
                if ask_if_it_helped(solution):
                    return solution
        return None

    def get_root(self):
        current_node = self
        while current_node.getParent():
            current_node = current_node.getParent()
        return current_node

    def toJSON(self):
        dict = {
            "question": self.data.doc.text,
            "solutions": [x.text for x in self.data.solutions],
            "children": [x for x in self.children]
        }
        return dict







