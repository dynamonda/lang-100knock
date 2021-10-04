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

def main():
    unittest.main()

if __name__ == '__main__':
    main()
