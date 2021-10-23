import q027
from typing import Dict
import re

"""28. MediaWikiマークアップの除去

27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．
"""

def pull_template_erase_strong_link_markup() -> Dict[str, str]:
    dic = q027.pull_template_erase_strong_link()
    for k in dic.keys():
        v: str = dic[k]
        v = v.replace('{{0}}', '0')         # {{0}}の消去
        v = v.replace('<br />', '')         # <br />の消去
        v = re.sub(r'<ref(.*?)</ref>', '', v, flags=re.DOTALL)  # <ref>~</ref>
        v = re.sub(r'<ref .* />', '', v)
        v = re.sub(r'{{.*\|(.*)\|.*\|.*}}', '\\1', v)
        v = re.sub(r'{{.*\|.*\|(.*)(}}|）)', '\\1', v)
        dic[k] = v
    return dic

def main():
    for k, v in pull_template_erase_strong_link_markup().items():
        print("{}: {}".format(k, v))

if __name__ == '__main__':
    main()