import q020
import re
from functools import reduce
from itertools import chain
from typing import Tuple, List

"""24. ファイル参照の抽出

記事から参照されているメディアファイルをすべて抜き出せ
"""

def pull_ref_file() -> List[str]:
    lines = list(filter(lambda x: "ファイル" in x, q020.read_data_uk().splitlines()))

    def ref_file(line) -> List[str]:
        return re.findall(r'\[\[ファイル:(.+?)\|', line)

    return list(reduce(chain, map(ref_file, lines)))

def main():
    print(pull_ref_file())

if __name__ == '__main__':
    main()
