from utils.utils import ask_if_it_helped, get_doc_from_input
from preprocess import preprocess
from copy import copy

class SpaCyTreeNode:

  def __init__(self, nlp_obj, typical_answer, solutions=None):
    self.doc = nlp_obj
    self.typical_answer = typical_answer
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
    return self.typical_answer.similarity(other)

  def similarityValueByQuestion(self, other):
    return self.doc.similarity(other)

  def pick_solution(self, data):
    user_problem = data

    def sort_by_similarity(e):
      return e[0].similarity(user_problem)

    local_solutions = copy(self.solutions)
    local_solutions.sort(key=sort_by_similarity, reverse=True)

    return local_solutions

  def add_solution(self, answer, solution):
    self.solutions.append([answer, solution])

  #TODO zrobic generacje z modelu
  def generate_question(self, user_solution):
    future_solution = user_solution
    user_question = get_doc_from_input("What would you ask next user to get your answer? >")
    return user_question
