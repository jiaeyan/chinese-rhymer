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

    # z/c/s + i -> z/c/s + I
    if re.match(r'[zcs]i$', pinyin):
        return pinyin.replace('i', 'I')

    # zh/ch/sh/r + i -> zh/ch/sh/r + II
    elif re.match(r'(?:zh|ch|sh|r)i$', pinyin):
        return pinyin.replace('i', 'II')

    # j/q/x/y + u/ue/un/uan -> j/q/x + v/ve/vn/van | v/ve/vn/van
    elif re.match(r'[jqxy]u', pinyin):
        return re.sub(r'y*(.+)', r'\1', pinyin.replace('u', 'v'))

    # y + a/e/ao/ou/an/ in/iang/ing/iong -> ia/ie/iao/iou/ian/ in/iang/ing/iong
    elif pinyin.startswith("y"):
        return re.sub(r'yi*(.*)', r'i\1', pinyin)

    # w + u/a/o/ai/ei/an/en/ang/eng        -> u/ua/uo/uai/uei/uan/uen/uang/ueng
    elif pinyin.startswith("w"):
        return re.sub(r'wu*(.*)', r'u\1', pinyin)

    # qiu -> qiou
    elif pinyin.endswith('iu'):
        return pinyin.replace('iu', 'iou')

    # cui -> cuei
    elif pinyin.endswith('ui'):
        return pinyin.replace('ui', 'uei')

    # lun -> luen
    elif pinyin.endswith('un'):
        return pinyin.replace('un', 'uen')

    return pinyin


def split_cv(pinyin):
    return re.findall(r'(ch|zh|sh|[^aeiIouv])*(.+)', pinyin)[0]


def vowel_parser(vowel: str) -> List[str]:
    if vowel == 'van':
        return ['v', 'an']

    elif len(vowel) > 1 and vowel[0] == 'u':
        return ['u', vowel[1:]]

    # for 'i', except 'in' and 'ing' (one vowel), 'ie' and 'ian' (sound different from 'e' and 'an')
    elif len(vowel) > 1 and vowel[0] == 'i' and vowel[1] != 'n' and vowel[1] != 'e' and vowel[1:] != 'an':
        return ['i', vowel[1:]]

    return [vowel]
