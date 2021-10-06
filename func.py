from typing import List, Dict, Set
from operator import add
from functools import reduce
from random import shuffle


class q000:
    @classmethod
    def reverse(cls, text: str) -> str:
        return text[::-1]


class q001:
    @classmethod
    def extract(cls, text: str) -> str:
        """文字列の1,3,5,7文字目を取り出して連結した文字列"""
        return text[:8:2]


class q002:
    @classmethod
    def mix_str(cls, text1: str, text2: str) -> str:
        """文字を先頭から交互に連結した文字列を返す"""
        return ''.join(reduce(add, zip(text1, text2)))


class q003:
    @classmethod
    def word_len_list(cls, text: str) -> List[int]:
        """文字列を単語に分解し（,と.を削除），各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを返す"""
        return [len(x) for x in text.replace(',', '').replace('.', '').split(' ')]


class q004:
    @classmethod
    def pos_map(cls, text: str) -> Dict[str, int]:
        """
        1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を返す
        """
        l = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        return {s[:1] if i+1 in l else s[:2]: i+1 for i, s in enumerate(text.split(' '))}


class q005:
    @classmethod
    def char_n_gram(cls, text: str, n: int) -> List[str]:
        """文字N-gramを返す"""
        return [text[i:i+n] for i in [x for x in range(0, len(text), n)]]

    @classmethod
    def word_n_gram(cls, text: str, n: int) -> List[str]:
        """単語N-gramを返す"""
        return [s[:n] for s in text.split(' ')]


class q006:
    @classmethod
    def text_add_set(cls, text1: str, text2: str) -> Set[str]:
        """和集合を返す"""
        return {s for s in text1} | {s for s in text2}

    @classmethod
    def text_product_set(cls, text1: str, text2: str) -> Set[str]:
        """積集合を返す

        集合A集合Bの両方に含まれている要素の集合
        """
        return {s for s in text1} & {s for s in text2}

    @classmethod
    def text_sub_set(cls, text1: str, text2: str) -> Set[str]:
        """差集合を返す"""
        return {s for s in text1} - {s for s in text2}


class q007:
    @classmethod
    def get_text(cls, x: str, y: str, z: str) -> str:
        return '{}時の{}は{}'.format(x, y, z)


class q008:
    @classmethod
    def encrypt(cls, text: str) -> str:
        """暗号化"""
        return ''.join([chr(219 - ord(c)) for c in text])

    @classmethod
    def decrypt(cls, enc: str) -> str:
        """複合化"""
        return ''.join([chr(219 - ord(e)) for e in enc])


class q009:
    @classmethod
    def shuffle_text(cls, text: str) -> str:
        """
        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
        それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
        ただし，長さが４以下の単語は並び替えないこととする．
        """
        def random(x):
            if len(x) > 4:
                start, middle, end = x[0], [s for s in x[1:len(x)-1]], x[-1]
                shuffle(middle)
                return start + ''.join(middle) + end
            return x

        return ' '.join(map(random, [s for s in text.split(' ')]))
