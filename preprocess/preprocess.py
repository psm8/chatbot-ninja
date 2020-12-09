import spacy

nlp = spacy.load("en_core_web_sm")
# tagger parser and ner added by default
# self.nlp.add_pipe(self.nlp.create_pipe("entity_linker"))
# self.nlp.add_pipe(self.nlp.create_pipe("textcat"))
nlp.add_pipe(nlp.create_pipe("entity_ruler"))
nlp.add_pipe(nlp.create_pipe("sentencizer"))

def preprocess(input):
    return nlp(input)

def tokenize(data):
    dict = {}
    for token in data:
        dict[token.text] = token.pos_
    return dict
