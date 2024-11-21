#coding:utf-8
import os
import json
import re

def parseRawData(author=None, constrain=None):
    rst = []

    def sentenceParse(para):
        result, number = re.subn("（.*?）", "", para)  # 简化匹配
        result, number = re.subn("{.*?}", "", result)
        result, number = re.subn("《.*?》", "", result)
        result, number = re.subn("[\[\]]", "", result)  # 修正无效转义序列
        r = ""
        for s in result:
            if s not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']:
                r += s
        r, number = re.subn("。。", "。", r)
        return r

    def handleJson(file):
        rst = []
        with open(file, 'r', encoding='utf-8') as f:  # 指定编码
            data = json.loads(f.read())
        for poetry in data:
            pdata = ""
            if (author is not None and poetry.get("author") != author):
                continue
            p = poetry.get("paragraphs")
            flag = False
            for s in p:
                sp = re.split("[，！。]", s)  # 去掉 .decode("utf-8")
                for tr in sp:
                    if constrain is not None and len(tr) != constrain and len(tr) != 0:
                        flag = True
                        break
                    if flag:
                        break
            if flag:
                continue
            for sentence in poetry.get("paragraphs"):
                pdata += sentence
            pdata = sentenceParse(pdata)
            if pdata != "":
                rst.append(pdata)
        return rst

    data = []
    src = 'tangshi/json/'
    for filename in os.listdir(src):
        if filename.startswith("poet.tang"):
            data.extend(handleJson(os.path.join(src, filename)))  # 使用 os.path.join
    return data
