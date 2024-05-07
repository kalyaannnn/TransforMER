from pathlib import Path

def get_config():
    return {
        "batch_size" : 8,
        "num_epochs" : 15,
        "lr" : 10**-4,
        "seq_length" : 350,
        "d_model" : 512,
        "lang_src" : "en",
        "lang_tgt" : "it",
        "model_folder" : "weights",
        "model_filename" : "tmodel_",
        "preload" : None,
        "tokenizer_file" : "tokenizer(0).json",
        "experiment_name" : "runs/tmodel"
    }

def get_weights_file_path(config, epoch : str):
    model_folder = config['model_folder']
    model_basename = config['model_basename']
    model_filename = f"{model_basename}{epoch}.pt"
    return str(Path('.') / model_folder / model_filename)