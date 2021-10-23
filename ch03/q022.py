import q021
import re
from typing import List

def pull_category_names() -> List[str]:
    """22.カテゴリ名の抽出
    
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．"""
    return list(map(lambda x: re.findall(r':(.+?)[\]|\|]', x), \
        q021.pull_category_lines()))

def main():
    print(pull_category_names())

if __name__ == '__main__':
    main()
