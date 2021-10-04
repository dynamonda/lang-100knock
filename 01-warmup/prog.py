import argparse

def q000():
    """
    00. 文字列の逆順Permalink
    文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    """
    text = 'stressed'
    print(text + ' => 逆順' + text[::-1])

def exec(number: int):
    if number == 0:
        q000()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='問題番号')
    args = parser.parse_args()

    print('number=' + (str)(args.number))

    exec(args.number)

if __name__ == '__main__':
    main()
