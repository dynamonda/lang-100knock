import q020
from typing import List

"""21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ．
"""

def pull_category_lines() -> List[str]:
    uk_data: str = q020.read_data_uk()
    return list(filter(lambda x: "[[Category" in x, uk_data.splitlines()))

def main():
    print(pull_category_lines())

if __name__ == '__main__':
    main()
