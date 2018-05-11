#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from pypinyin.phrases_dict import phrases_dict
from chrhyme.parser import word_parser

vocab = set()


with open('data/cidian.txt', 'r', encoding='gb18030') as f:
    for line in f:
        if '【' in line:
            words = re.findall(r'【([\u4E00-\u9FA5，]+?)】', line.strip())
            for word in words:
                if len(word) > 1:
                    vocab.add(word)

print('+ 现代汉语词典 (含俗语)：', len(vocab))


with open('data/chengyu.txt', 'r', encoding='gb18030') as f:
    for line in f:
        if "拼音" in line:
            words = re.findall(r'([\u4E00-\u9FA5，\s]+?)拼音.+', line.strip())
            for word in words:
                word = word.strip()
                if len(word) > 1:
                    vocab.add(word)

print('+ 成语词典 (含俗语)：', len(vocab))


with open('data/dict.txt', 'r') as f:
    for line in f:
        word = line.strip().split()[0]
        if len(word) > 1 and re.match(r'^[\u4E00-\u9FA5，]+$', word):
            vocab.add(word)

print('+ 各大输入法词库 (无俗语，含英语)：', len(vocab))


for words in phrases_dict:
    for word in words.split('，'):
        vocab.add(word.strip())

print('+ 自带词库 (无俗语)：', len(vocab))


look_up = defaultdict(list)
for word in vocab:
    pinyins = word_parser(word)
    if len(word) > 1:
        look_up[tuple([pinyin[1][-1] for pinyin in pinyins[-2:]])].append(word)
    if len(word) > 2:
        look_up[tuple([pinyin[1][-1] for pinyin in pinyins[-3:]])].append(word)
    if len(word) > 3 and word[-4] != '，':
        look_up[tuple([pinyin[1][-1] for pinyin in pinyins[-4:]])].append(word)

with open('phrase_dict.txt', 'w') as f:
    for k, v in look_up.items():
        f.write('{}\t{}\n'.format(' '.join(list(k)), ' '.join(sorted(v))))
    print('done!')


# with open('phrase_dict.py', 'w') as f:
#     f.write('phrase_dict = {\n')
#     for k, v in look_up.items():
#         f.write('\t{}:{},\n'.format(k, sorted(v)))
#     f.write('}')
#     print('done!')
