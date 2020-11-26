import pandas as pd
from pprint import pprint
from t5.model import get_model

model = get_model()

df = pd.read_csv("data/eval_df.tsv", sep="\t").astype(str)
preds = model.predict(
    ["ask_question: " + description for description in df["input_text"].tolist()]
)

questions = df["target_text"].tolist()

with open("test_outputs_large/generated_questions_sampling.txt", "w") as f:
    for i, desc in enumerate(df["input_text"].tolist()):
        pprint(desc)
        pprint(preds[i])
        print()

        f.write(str(desc) + "\n\n")

        f.write("Real question:\n")
        f.write(questions[i] + "\n\n")

        f.write("Generated questions:\n")
        for pred in preds[i]:
            f.write(str(pred) + "\n")
        f.write("________________________________________________________________________________\n")