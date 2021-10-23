import q020
import re
from typing import Tuple, List

"""23. セクション構造

記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ
"""

def section_level() -> List[Tuple[str, int]]:
    section_list = list( \
        filter(lambda x: re.match(r'=+?(.+?)=+?', x) is not None, \
        q020.read_data_uk().splitlines()))
    
    def pull_section_level(s):
        m_list = re.findall(r'(=+?)([^=]+?)=+?', s)
        if len(m_list) == 0:
            return ("None", 0)
        level, name = m_list[0]
        return (name, len(level) - 1)

    return list(map(pull_section_level, section_list))

def main():
    print(section_level())

if __name__ == '__main__':
    main()
