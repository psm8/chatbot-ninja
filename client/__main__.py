import argparse

from preprocess.preprocess import Preprocess
from t5.model import get_model


def main():

    # preprocess = Preprocess()
    model = get_model()

    while True:
        model.predict("I remove the engine!	ask_question")
        inp = input(">")
        # preprocessed_input = preprocess.preprocess(inp)
        # for token in preprocessed_input:
        #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #           token.shape_, token.is_alpha, token.is_stop)
        # for ent in preprocessed_input.ents:
        #     print(ent.text, ent.start_char, ent.end_char, ent.label_)
        # for word in preprocessed_input:
        #     lexeme = preprocessed_input.vocab[word.text]
        #     print(lexeme.text, lexeme.orth, lexeme.shape_, lexeme.prefix_, lexeme.suffix_,
        #           lexeme.is_alpha, lexeme.is_digit, lexeme.is_title, lexeme.lang_)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Chatbot Ninja")
    # parser.add_argument("example1")
    # options = parser.parse_args()
    #
    # example1 = options.example1
    # main(example1=example1)
    main()
