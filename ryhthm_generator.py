from parser import word_parser
from phrase_dict import phrase_dict


nun_ryhthms = {1: '单押词', 2: '双押词', 3: '三押词', 4: '四押词'}


def valid_cv(word_pinyins, target_pinyins, con_ids, vow_ids):
    for c in con_ids:
        # if consonant of target pinyin is empty, it matches any consonant in the word pinyin
        if target_pinyins[c][0] and word_pinyins[c][0] != target_pinyins[c][0]:
            return False

    for v in vow_ids:
        word_v = word_pinyins[v][1]
        target_v = target_pinyins[v][1]
        if len(target_v) == 1 and word_v[-1] != target_v[-1]:
            return False
        elif len(target_v) == 2 and "".join(word_v) != "".join(target_v):
            return False

    return True


def get_candidates(pinyins, c, v):
    con_ids = [int(c_pos) - 1 for c_pos in list(c)] if c != '0' else []
    vow_ids = [int(v_pos) - 1 for v_pos in list(v)] if v != '0' else []

    hash_vowels = tuple([pinyin[1][-1] for pinyin in pinyins])

    try:
        basic_candidates = phrase_dict[hash_vowels]
    except KeyError:
        return []

    parsed_candidates = [(word, word_parser(word)) for word in basic_candidates]
    qualified_candidates = []

    for word, word_pinyins in parsed_candidates:
        if valid_cv(word_pinyins, pinyins, con_ids, vow_ids):
            qualified_candidates.append(word)

    return qualified_candidates


def generate_rhythms():
    while 1:
        word = input('◼︎ 请输入一个你想押韵的词(按回车退出): ').strip()
        if word:
            # num = input('请输入要押韵字的个数(阿拉伯数字)，请限制在输入词的长度以下: ')
            # more = input('是否要输出押韵字个数以下所有可能的押韵词？请输入"yes"或"no": ')
            cons = input('\t-是否押声母？例如对于"欢喜"，押"还席"不押"惯技"。\n\t 请输入要押声母的字的位置\n\t (0-不押；1-押"欢"；2-押"喜"；12-押"欢喜"): ')
            fullv = input('\t-是否押全韵母？例如对于"欢喜"，押"端倪"不押"叹息"。\n\t 请输入要押全韵母的字的位置\n\t (0-不押；1-押"欢"；2-押"喜"；12-押"欢喜"): ')
            num_char = len(word)
            pinyins = word_parser(word)
            candidates = get_candidates(pinyins, cons, fullv)
            if candidates:
                print('>>> {}: {}'.format(nun_ryhthms[num_char], candidates))
            else:
                print('>>> 太可惜了，没有适合押韵的词！请尝试分解押韵，例如将"光明磊落"分为"光明"和"磊落"分别进行查询。')
        else:
            break


generate_rhythms()