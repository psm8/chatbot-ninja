from utils.utils import ask_if_it_helped, get_doc_from_input

class SpaCyTreeNode:

  def __init__(self, nlp_obj, solutions=None):
    self.doc = nlp_obj
    if solutions is None:
      self.solutions = []
    else:
      self.solutions = solutions

  def __eq__(self, other):
    if isinstance(other, SpaCyTreeNode):
      return self.doc.text == other.doc.text
    return False

  def __str__(self):
    return self.doc.text

  def similarityValue(self, other):
    return self.doc.similarity(other)

  def pick_solution(self, data):
    user_problem = data
    def sort_by_similarity(e):
      return e.similarity(user_problem)

    return self.solutions.sort(key=sort_by_similarity)

  def add_solution(self, solution):
    self.solutions.append(solution)

  #TODO zrobic generacje z modelu
  def generate_question(self, user_solution):
    future_solution = user_solution
    user_question = get_doc_from_input("What would you ask next user to get your answer? >")
    return user_question