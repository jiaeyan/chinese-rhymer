#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from typing import List, Tuple
from pypinyin import lazy_pinyin


def word_parser(word: str) -> List[Tuple[str, List[str]]]:
    pinyins: List[str] = lazy_pinyin(word)
    return pinyin_parser(pinyins)


def pinyin_parser(pinyins: List[str]) -> List[Tuple[str, List[str]]]:
    parsed_pinyins = []
    for pinyin in pinyins:
        pinyin = pinyin_correction(pinyin)
        consonant, vowel = split_cv(pinyin)
        parsed_pinyins.append((consonant, vowel_parser(vowel)))
    return parsed_pinyins


def pinyin_correction(pinyin: str) -> str:

    # j/q/x/y + u/ue/un/uan -> j/q/x + v/ve/vn/van | v/ve/vn/van
    if re.match(r'[jqxy]u', pinyin):
        return re.sub(r'y*(.+)', r'\1', pinyin.replace("u", "v"))

    # y + a/e/ao/ou/an/ in/iang/ing/iong -> ia/ie/iao/iou/ian/ in/iang/ing/iong
    elif pinyin.startswith("y"):
        return re.sub(r'yi*(.*)', r'i\1', pinyin)

    # w + u/a/o/ai/ei/an/en/ang/eng        -> u/ua/uo/uai/uei/uan/uen/uang/ueng
    elif pinyin.startswith("w"):
        return re.sub(r'wu*(.*)', r'u\1', pinyin)

    # qiu -> qiou
    elif pinyin.endswith("iu"):
        return pinyin.replace("iu", "iou")

    # cui -> cuei
    elif pinyin.endswith("ui"):
        return pinyin.replace("ui", "uei")

    # lun -> luen
    elif pinyin.endswith("un"):
        return pinyin.replace("un", "uen")

    return pinyin


def split_cv(pinyin):
    return re.findall(r'(ch|zh|sh|[^aeiouv])*(.+)', pinyin)[0]


def vowel_parser(vowel: str) -> List[str]:
    if vowel == 'van':
        return ['v', 'an']

    elif len(vowel) > 1 and vowel[0] == 'u':
        return ['u', vowel[1:]]

    # for 'i', except 'in' and 'ing' (one vowel), 'ie' and 'ian' (sound different from 'e' and 'an')
    elif len(vowel) > 1 and vowel[0] == 'i' and vowel[1] != 'n' and vowel[1] != 'e' and vowel[1:] != "an":
        return ['i', vowel[1:]]

    return [vowel]

# ('e', 'ang', 'eng', 'ing') ['月朗风清']
# py = ['yan', 'han']
# consonant, vowel = re.findall(r'(ch|zh|sh|[^aeiou])*(.+)', 'u')[0]
# print(consonant, vowel)
# print(pinyin_parser(py))

# print(pinyin_correction('yue'))
# word = '月朗风清'
# print(word_parser(word))

# py = 'iao'
# print(vowel_parser(py))


# w = '三十年河东，三十年河西'
# print(w.split('，'))




