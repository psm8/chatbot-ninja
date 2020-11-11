class Answer():

    def __init__(self, doc, question):
        self.sentences = doc.sents
        self.question = question
        self.answer_meaning_value = doc.vector


    def