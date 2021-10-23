import json
from typing import List, Dict

"""
20. JSONデータの読み込みPermalink
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

def read_data() -> List[Dict]:
    with open('data/jawiki-country.json', 'r') as f:
        # まさかの複数のjsonオブジェクト入りファイルだった。。。
        # json.loads(f.read())　じゃだめだった
        objs = list()
        for line in f.readlines():
            dic = json.loads(line)
            objs.append(dic)
        return objs

def read_data_uk() -> str:
    """イギリスの記事本文を返す"""
    obj_list: List = read_data()
    uk = list(filter(lambda obj: obj['title'] == 'イギリス', obj_list))
    return uk[0]['text']

if __name__ == '__main__':
    print(read_data_uk())
