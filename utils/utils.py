from preprocess import preprocess


def ask_if_it_helped():
    yes = preprocess.preprocess("yes")
    no = preprocess.preprocess("no")

    answer = get_doc_from_input("Was it helpfull")

    if yes.similarity(answer) - no.similarity(answer) > 0:
        return True

    else:
        return False


def get_doc_from_input(message):
    user_input = input(message)
    return preprocess.preprocess(user_input)

