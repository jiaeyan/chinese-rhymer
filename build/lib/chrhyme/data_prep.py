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
            words = re.findall(r'【(.+?)】', line.strip())[0].split('，')
            for word in words:
                vocab.add(word.strip())

with open('data/chengyu.txt', 'r', encoding='gb18030') as f:
    for line in f:
        if "拼音" in line:
            words = re.findall(r'(.+?)拼音.+', line.strip())[0].strip().split('，')
            for word in words:
                vocab.add(word.strip())

for words in phrases_dict:
    for word in words.split('，'):
        vocab.add(word.strip())

look_up = defaultdict(list)
for word in vocab:
    pinyins = word_parser(word)
    look_up[tuple([pinyin[1][-1] for pinyin in pinyins])].append(word)

with open('phrase_dict.py', 'w') as f:
    f.write('phrase_dict = {\n')
    for k, v in look_up.items():
        f.write('\t{}:{},\n'.format(k, sorted(v)))
    f.write('}')
    print('done!')
