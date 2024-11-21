import torch
import torch.autograd as autograd

def make_one_hot_vec(word, word_to_ix):
    rst = torch.zeros(1, 1, len(word_to_ix))
    rst[0][0][word_to_ix[word]] = 1
    return autograd.Variable(rst)

def make_one_hot_vec_target(word, word_to_ix):
    return autograd.Variable(torch.LongTensor([word_to_ix[word]]))

def prepare_sequence(seq, word_to_ix):
    idxs = [word_to_ix[w] for w in seq]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)

def toList(sen):
    return list(sen)

def invert_dict(d):
    return {v: k for k, v in d.items()}
