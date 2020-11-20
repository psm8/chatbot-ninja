import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM

class Tokenizer:

    def __init__(self):
        # Load pre-trained model (weights)
        model_version = 'bert-base-uncased'
        self.model = BertForMaskedLM.from_pretrained(model_version)
        self.model.eval()
        self.cuda = torch.cuda.is_available()
        if self.cuda:
            self.model = self.model.cuda()

        # Load pre-trained model tokenizer (vocabulary)
        self.tokenizer = BertTokenizer.from_pretrained(model_version, do_lower_case=model_version.endswith("uncased"))

    def tokenize_batch(self, batch):
        return [self.tokenizer.convert_tokens_to_ids(sent) for sent in batch]

    def untokenize_batch(self, batch):
        return [self.tokenizer.convert_ids_to_tokens(sent) for sent in batch]

    def detokenize(self, sent):
        """ Roughly detokenizes (mainly undoes wordpiece) """
        new_sent = []
        for i, tok in enumerate(sent):
            if tok.startswith("##"):
                new_sent[len(new_sent) - 1] = new_sent[len(new_sent) - 1] + tok[2:]
            else:
                new_sent.append(tok)
        return new_sent
