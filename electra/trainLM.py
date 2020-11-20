import wandb
from simpletransformers.language_modeling import LanguageModelingModel

def trainLM():
    wandb.init()


    # configure your model
    train_args = {
        "reprocess_input_data": False, "overwrite_output_dir": True, "num_train_epochs": 2,
        "save_eval_checkpoints": True, "save_model_every_epoch":
            False, "learning_rate": 3e-2, "warmup_steps": 1000, "train_batch_size": 64,
        "eval_batch_size": 128, "fp16": False, "gradient_accumulation_steps": 1,
        "block_size": 128, "max_seq_length": 128, "dataset_type": "simple",
        'wandb_project': "simpletransformers", "wandb_kwargs": {"name": "LM3e-2"},
        "logging_steps": 100, "evaluate_during_training": True, "evaluate_during_training_steps":
            50000, "evaluate_during_training_verbose": True,
        "use_cached_eval_features": True, "sliding_window": True, "vocab_size": 20000,
        "generator_config": {
            "embedding_size": 128,
            "hidden_size": 256,
            "num_hidden_layers": 3,
        },
        "discriminator_config": {
            "embedding_size": 128,
            "hidden_size": 256,
        },
    }
    train_file = "train.txt"
    test_file = "test.txt"

    # Initialize a LanguageModelingModel
    model = LanguageModelingModel(
        "electra",
        None,
        args=train_args,
        train_files=train_file,
    )

    # Train the model
    model.train_model(
        train_file, eval_file=test_file,
    )
