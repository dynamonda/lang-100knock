import q026
from typing import Dict
import re

"""27. 内部リンクの除去

26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．

処理1. [[***|$$$]] => [[$$$]]
処理2. [[@@@]] => @@@
の2段階 
"""

def pull_template_erase_strong_link() -> Dict[str, str]:
    dic = q026.pull_template_erase_strong()
    for k in dic.keys():
        v: str = dic[k]
        v = re.sub(r'\[\[.*?\|(.*?)\]\]', '[[\\1]]', v) # 処理1
        v = re.sub(r'\[\[(.*?)\]\]', '\\1', v)          # 処理2
        dic[k] = v
    return dic

def main():
    for k, v in pull_template_erase_strong_link().items():
        print("{}: {}".format(k, v))

if __name__ == '__main__':
    main()