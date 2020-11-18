class spaCyTreeNode():
  def __init__(self, doc, qa_tag):

    # here we will save the whole document to ensure that we have all necessary values
    self.doc = doc
    # qa_tag is responsible for letting you now if it is a Answer or Question node
    # and to choose which after-process select and run
    self.qa_tag = qa_tag

  def similarityValue(self, other):
    self.doc.similarity(other.doc)

  def tokenTextAndTags(self):
    dict ={}
    for token in self.doc:
      dict[token.text] = token.pos_
    return dict