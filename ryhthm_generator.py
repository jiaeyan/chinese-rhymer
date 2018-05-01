from pypinyin import lazy_pinyin
from parser import word_parser
from phrase_dict import phrase_dict


def get_vowels(pinyins):
    return tuple([pinyin[1][-1] for pinyin in pinyins])


def get_consonants(pinyins):
    return tuple([pinyin[0] for pinyin in pinyins])


def get_candidates(pinyins, num, more, cons, fullv):
    vowels = get_vowels(pinyins)
    conss = get_consonants(pinyins)
    return phrase_dict[vowels]


def generate_rhythms():
    while 1:
        word = input('请输入一个你想押韵的词(按回车退出): ')
        if word:
            num = input('请输入要押韵字的个数(阿拉伯数字)，请限制在输入词的长度以下: ')
            more = input('是否要输出押韵字个数以下所有可能的押韵词？请输入"yes"或"no": ')
            cons = input('是否要押声母？例如对于"欢"，押"患"不押"川"。请输入"yes"或"no": ')
            fullv = input('是否要押全韵母？例如对于"欢"，押"乱"不押"烂"。请输入"yes"或"no": ')
            pinyins = word_parser(word)
            candidates = get_candidates(pinyins, num, more, cons, fullv)
            if candidates:
                print(candidates)
            else:
                print('太可惜了，没有适合押韵的词！请尝试分解押韵，例如将"光明磊落"分为"光明"和"磊落"分别进行查询。')
        else:
            break


generate_rhythms()