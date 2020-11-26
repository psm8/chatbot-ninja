from preprocess import preprocess


def ask_if_it_helped():
    yes = preprocess.preprocess("yes")
    no = preprocess.preprocess("no")

    control_question = input("Was it helpful?")
    answer = preprocess.preprocess(control_question)

    if yes.similarity(answer) - no.similarity(answer) > 0:
        return True

    else:
        return False
