from sentence.spaCyTreeNode import SpaCyTreeNode


class Node:
    def __init__(self, data):
        self.data = SpaCyTreeNode(data)
        self.children = []
        self.parent = None
        self.level = 0

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

    def search_branch(self, data, treshold):
        base_boarder = treshold
        similarity = base_boarder
        best_match = None
        list = self.getChildren()
        for i in range(0, len(list)):
            result = list[i].getData().similarityValue(data)
            if result > similarity:
                best_match = list[i]
                similarity = result
        print(similarity)
        return best_match

    def search_other_branches(self, data, treshold):
        base_boarder = treshold
        similarity = base_boarder
        best_match = None
        current_node = self

        while current_node.getParent():
            current_node = current_node.getParent()

        list = current_node.getChildren()

        while list[0].getLevel() <= self.getLevel():
            result = list[0].getData().similarityValue(data)
            if result > similarity and not self == list[0]:
                best_match = list[0]
                similarity = result
            current_node = list[0]
            current_node_children = current_node.getChildren()

            # for i in list:
            #     print(i)

            list.pop(0)
            if len(current_node_children) > 0:
                for i in range(0, len(current_node_children)):
                    list.append(current_node_children[i])
            if len(list) == 0:
                break
        #     print("\n*** one iter of while ***\n")
        # print("\n*** one method called ***\n")
        print(similarity)
        return best_match

    # Do zmiany zeby od razu tu leciał check czy rozwiazanie pasuje
    def add_solutions(self, solution):
        self.data.add_solution(solution)

    def generate_question(self, user_solution):
        new_question = self.data.generate_question(user_solution)
        new_child = Node(new_question)
        self.addChild(new_child)
        new_child.add_solutions(user_solution)




