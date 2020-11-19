from preprocess.preprocess import Preprocess

class SpaCyTreeNode():
  def __init__(self, doc):

    # here we will save the whole document to ensure that we have all necessary values
    self.doc = doc
    self.solutions = []

  def similarityValue(self, other):
    return self.doc.similarity(other.doc)

  def tokenTextAndTags(self):
    dict ={}
    for token in self.doc:
      dict[token.text] = token.pos_
    return dict

  def add_solution(self, solution):
    self.solutions.append(solution)

  def generate_question(self, user_solution):
    preprocess = Preprocess()
    user_question = preprocess.preprocess(input("What would you ask next user to get your answer? >"))
    return user_question