import pandas as pd

from simpletransformers.t5 import T5Model


def training():

    train_df = pd.read_csv("data/train_df.tsv", sep="\t").astype(str)
    eval_df = pd.read_csv("data/eval_df.tsv", sep="\t").astype(str)

    model_args = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "train_batch_size": 1,
        "num_train_epochs": 1,
        "save_eval_checkpoints": True,
        "save_steps": -1,
        "use_multiprocessing": False,
        "evaluate_during_training": True,
        "evaluate_during_training_steps": 15000,
        "evaluate_during_training_verbose": True,
        "fp16": False,


        "wandb_project": "Question Generation with T5",
    }

    model = T5Model("t5-base", args=model_args, use_cuda=False)

    model.train_model(train_df, eval_data=eval_df, use_cuda=False)


if __name__ == '__main__':
    training()