from simpletransformers.t5 import T5Model


def get_model():
    model_args = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "eval_batch_size": 32,
        "num_train_epochs": 1,
        "save_eval_checkpoints": False,
        "use_multiprocessing": False,
        "num_beams": None,
        "do_sample": True,
        "max_length": 50,
        "top_k": 50,
        "top_p": 0.95,
        "num_return_sequences": 3,
    }

    return T5Model("outputs/checkpoint-15000", args=model_args, use_cuda=False)