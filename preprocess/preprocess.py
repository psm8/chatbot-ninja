import spacy


class Preprocess:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        # tagger parser and ner added by default
        # self.nlp.add_pipe(self.nlp.create_pipe("entity_linker"))
        # self.nlp.add_pipe(self.nlp.create_pipe("textcat"))
        self.nlp.add_pipe(self.nlp.create_pipe("entity_ruler"))
        self.nlp.add_pipe(self.nlp.create_pipe("sentencizer"))

    def preprocess(self, input):
        print(self.nlp.pipe_names)
        doc = self.nlp(input)

        return doc
