from preprocess import preprocess


def ask_if_it_helped(solution):
    print(solution.text)
    yes = preprocess.preprocess("yes")
    no = preprocess.preprocess("no")

    answer = preprocess.preprocess(input("Was it helpfull"))

    if yes.similarity(answer) - no.similarity(answer) > 0:
        print("You're welcome")
        return True

    else:
        return False




def get_doc_from_input(message):
    user_input = input(message)
    return preprocess.preprocess(user_input)


def similarity_with_wrong_answer(self, user_input):
    self.wrong_answer = [preprocess.preprocess(x) for x in ["That is not what I meant", "You are wrong",
                                                            "You are misunderstanding me", "You don't understand", "no"]]
    return max([x.similarity(user_input) for x in self.wrong_answer])
