import argparse
import unittest

class Test00(unittest.TestCase):
    def test_q000(self):
        """
        00. 文字列の逆順Permalink
        文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
        """
        text = 'stressed'
        answer = text[::-1]

        self.assertEqual(answer, 'desserts')

    def test_q001(self):
        """
        01. 「パタトクカシーー」Permalink
        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
        """
        text = 'パタトクカシーー'
        answer = text

        self.assertEqual(answer, 'パトカー')

    def test_q002(self):
        """
        02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
        """
        text1 = 'パトカー'
        text2 = 'タクシー'
        answer = text1 + text2

        self.assertEqual(answer, 'パタトクカシーー')

    def test_q003(self):
        """
        03. 円周率Permalink
        “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を
        単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

        ピリオド、カンマ排除しようか。
        """
        text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
        answer = []

        right_answer = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertListEqual(answer, right_answer)

    def test_q004(self):
        """
        04. 元素記号Permalink
        “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，
        1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
        """
        text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
        answer = {}

        right_answer = {
            'H': 1, 'He': 2, 
            'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10,
            'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18,
            'K': 19, 'Ca': 20
        }
        self.assertDictEqual(answer, right_answer)

    def test_q005(self):
        """
        05. n-gramPermalink
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ
        この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

        bi-gram: uni(1), bi(2), try(3)
        """
        text = 'I am an NLPer'
        char_bigram = []
        word_bigram = []
        self.assertListEqual(char_bigram, ['I ', 'am', ' a', 'n ', 'NL', 'Pe', 'r'])
        self.assertListEqual(word_bigram, ['I', 'am', 'an', 'NL'])

    def test_q006(self):
        """
        06. 集合Permalink
        “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
        それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
        さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
        """
        text1 = 'paraparaparadise'
        text2 = 'paragraph'
        add_set = {}
        product_set = {}    # 積集合、集合A集合Bの両方に含まれている要素の集合
        sub_set = {}

        self.assertSetEqual(add_set, {'p', 'a', 'r', 'g', 'p', 'h', 'd', 'i', 's', 'e'})
        self.assertSetEqual(product_set, {'p', 'a', 'r'})
        self.assertSetEqual(sub_set, {'d', 'i', 's', 'e'})

    def test_q007(self):
        """
        07. テンプレートによる文生成Permalink
        引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
        さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
        """
        x, y, z = '12', '気温', '22.4'
        answer = '' #func(x, y, z)
        self.assertEqual(answer, '12時の気温は22.4')

    def test_q008(self):
        """
        08. 暗号文Permalink
        与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

        英小文字ならば(219 - 文字コード)の文字に置換
        その他の文字はそのまま出力
        この関数を用い，英語のメッセージを暗号化・復号化せよ．
        """
        text = 'supercalifragilisticexpialidocious'
        enq_text = ''
        deq_text = ''
        self.assertEqual(deq_text, text)

    def test_q009(self):
        """
        09. TypoglycemiaPermalink
        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
        それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
        ただし，長さが４以下の単語は並び替えないこととする．
        適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
        """
        text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
        answer = ''

        # テスト
        self.assertRegex(answer, 'I c[ouldn’]{6}t b[eliev]{5}e that I c[oul]{3}d a[ctuall]{6}y u[nderstan]{8}d what I was r[eadin]{5}g : the p[henomena]{8}l p[owe]{3}r of the h[uma]{3}n mind .')

def main():
    unittest.main()

if __name__ == '__main__':
    main()
