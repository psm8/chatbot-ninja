from bert.bertMLC import BertMLC


def train():

    n_samples = 5
    batch_size = 5
    max_len = 40
    top_k = 100
    temperature = 1.0
    generation_mode = "parallel-sequential"
    leed_out_len = 5 # max_len
    burnin = 250
    sample = True
    max_iter = 500

    # Choose the prefix context
    seed_text = "[CLS]".split()
    bertMLC = BertMLC()
    bert_sents = bertMLC.generate(n_samples, seed_text=seed_text, batch_size=batch_size, max_len=max_len,
                          generation_mode=generation_mode,
                          sample=sample, top_k=top_k, temperature=temperature, burnin=burnin, max_iter=max_iter,
                          cuda=bertMLC.tokenizer.cuda)
    for sent in bert_sents:
        bertMLC.printer(sent, should_detokenize=True)


if __name__ == '__main__':
    train()
