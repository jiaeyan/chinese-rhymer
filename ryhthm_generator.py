from pypinyin import lazy_pinyin
from parser import word_parser
from phrase_dict import phrase_dict


word = input('请输入一个你想押韵的词: ')

pinyins = word_parser(word)
vowels = tuple([pinyin[1][-1] for pinyin in pinyins])
candidtes = phrase_dict[vowels]