import q025
from typing import Dict

"""26. 強調マークアップの除去

25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を
除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

def pull_template_erase_strong() -> Dict[str, str]:
    dic = q025.pull_template()
    for k in dic.keys():
        v: str = dic[k]
        dic[k] = v.replace("'''", '').replace("''", '')
    return dic

def main():
    print(pull_template_erase_strong())

if __name__ == '__main__':
    main()