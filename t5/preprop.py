import fnmatch
import os
import pandas as pd
from sklearn.model_selection import train_test_split


RIGHT_QUESTIONS = ["did you tr", "have you tr", "did you considered ", "you might "]


def parse(file):
    f = file.read()
    for l in f:
        yield eval(l)


def getDF(path):
    i = 0
    df = {}
    for d in parse(path):
        df[i] = d
        i += 1

    return pd.DataFrame.from_dict(df, orient='index')


def choose_right_questions(path):
    data = {'target_text':[], 'input_text':[], 'prefix':[]}
    for file in os.listdir(path):
        if fnmatch.fnmatch(file, 'dialogueText.csv'):
            print(file)
            df = pd.read_csv(path + "/" +file)
            df2 = df.drop(columns=['folder', 'date'])
            df3 = df2.groupby(['dialogueID'])

            for _, group in df3:
                for id1, text in group.iterrows():
                    if is_right_question(text['text']):
                        append_result(data, group, id1)

    result_df = pd.DataFrame.from_dict(data)
    result_df.to_csv(f"data/ninja_data_all.tsv", "\t")

    train_df, eval_df = train_test_split(result_df, test_size=0.05)

    train_df.to_csv("data/ninja_train_df2.tsv", "\t")
    eval_df.to_csv("data/ninja_eval_df2.tsv", "\t")


def is_right_question(text):
    if isinstance(text, str):
        for question in RIGHT_QUESTIONS:
            if question in text:
                return True
    return False


def append_result(data, group, id1):
    local_text = ''
    max_id = max([id_test for id_test, _ in group.iterrows()])
    if max_id > id1:
        for id2, text2 in group.iterrows():
            if id1 - 5 <= id2:
                if id2 < id1:
                    if isinstance(text2['text'], str):
                        local_text += (text2['text'] + " ")
                elif id2 == id1:
                    target_text = (text2['text'] + " ")
                else:
                    break

    if local_text != "":
        data['target_text'].append(target_text)
        local_text += text2['text']
        data['input_text'].append(local_text)
        data['prefix'].append('CHAT')


choose_right_questions('data-ubuntu/Ubuntu-dialogue-corpus')
