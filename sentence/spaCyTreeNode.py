from preprocess import preprocess


class SpaCyTreeNode:

  def __init__(self, text):
    self.doc = preprocess.preprocess(text)
    self.solutions = []

  def __eq__(self, other):
    if isinstance(other, SpaCyTreeNode):
      return self.doc.text == other.doc.text
    return False

  def __str__(self):
    return self.doc.text


  def similarityValue(self, other):
    return self.doc.similarity(preprocess.preprocess(other))

  def tokenTextAndTags(self):
    return preprocess.tokenize(self.doc)

  def add_solution(self, solution):
    self.solutions.append(preprocess.preprocess(solution))

  def generate_question(self, user_solution):
    future_solution = preprocess.preprocess(user_solution)
    user_question = input("What would you ask next user to get your answer? >")
    return user_question