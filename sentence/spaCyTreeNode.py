from preprocess import preprocess
from utils.utils import ask_if_it_helped

class SpaCyTreeNode:

  def __init__(self, text, solutions=None):
    self.doc = preprocess.preprocess(text)
    if solutions is None:
      self.solutions = []


  def __eq__(self, other):
    if isinstance(other, SpaCyTreeNode):
      return self.doc.text == other.doc.text
    return False

  def __str__(self):
    return self.doc.text


  def similarityValue(self, other):
    return self.doc.similarity(preprocess.preprocess(other))

  def pick_solution(self, data):
    user_problem = preprocess.preprocess(data)
    def sort_by_similarity(e):
      return e.similarity(user_problem)

    self.solutions.sort(key=sort_by_similarity)
    print(str(self.solutions))
    # best_solution = self.solutions[0]
    # max_similarity = best_solution.similarity(user_problem)
    # for solution in self.solutions:
    #   if max_similarity < solution.similarity(user_problem):
    #     best_solution = solution
    #     max_similarity = best_solution.similarity(user_problem)
    for solution in self.solutions:
      print(solution.text)
      # if solution > :
    return solution

  def tokenTextAndTags(self):
    return preprocess.tokenize(self.doc)

  def add_solution(self, solution):
    self.solutions.append(preprocess.preprocess(solution))

  def generate_question(self, user_solution):
    future_solution = preprocess.preprocess(user_solution)
    user_question = input("What would you ask next user to get your answer? >")
    return user_question