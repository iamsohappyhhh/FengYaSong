# coding:utf-8
import pickle as p
from utils import *

#选择‘tangshi.pt''songci.pt''yuanqu.pt'
model = torch.load('songci.pt')
max_length = 100
# 选择'wordDic_tangshi''wordDic_songci''wordDic_yuanqu'
with open('wordDic_songci', 'rb') as rFile:
    word_to_ix = p.load(rFile)  # 从文件中加载字典

def invert_dict(d):
    return dict((v, k) for k, v in d.items())


ix_to_word = invert_dict(word_to_ix)


# Sample from a category and starting letter
def sample(startWord='<START>'):
    input = make_one_hot_vec_target(startWord, word_to_ix)
    hidden = model.initHidden()
    output_name = "";
    if (startWord != "<START>"):
        output_name = startWord
    for i in range(max_length):
        output, hidden = model(input.cuda(), hidden)
        topv, topi = output.data.topk(1)
        topi = topi.item()
        w = ix_to_word[topi]
        if w == "<EOP>":
            break
        else:
            output_name += w
        input = make_one_hot_vec_target(w, word_to_ix)
    return output_name



print(sample("春"))
print(sample("花"))
print(sample("秋"))
print(sample("月"))
print(sample("夜"))
print(sample("山"))
print(sample("水"))
print(sample("风"))
print(sample("雪"))
print(sample("梅"))
print(sample("柳"))
print(sample("竹"))
print(sample("湖"))
print(sample("云"))
print(sample("霞"))
print(sample("雷"))
print(sample("雨"))
print(sample("天"))
print(sample("地"))
print(sample("人"))
print(sample("心"))
print(sample("梦"))
print(sample("诗"))
print(sample("情"))
print(sample("爱"))
print(sample("思"))
print(sample("静"))
print(sample("声"))
print(sample("光"))
print(sample("影"))
print(sample("花"))
print(sample("香"))
print(sample("鸟"))
print(sample("鱼"))
