class SpaCyTreeNode():
  def __init__(self, doc):

    # here we will save the whole document to ensure that we have all necessary values
    self.doc = doc

  def similarityValue(self, other):
    return self.doc.similarity(other.doc)

  def tokenTextAndTags(self):
    dict ={}
    for token in self.doc:
      dict[token.text] = token.pos_
    return dict