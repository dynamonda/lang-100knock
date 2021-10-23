import q028
import requests
from pprint import pprint

"""29. 国旗画像のURLを取得する

テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

https://www.mediawiki.org/wiki/API:Imageinfo#Python
"""

def get_image_url() -> str:
    dic = q028.pull_template_erase_strong_link_markup()

    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:{}".format(dic['国旗画像']),
        "iiprop": "url"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    image_url = None
    for _, v in DATA['query']['pages'].items():
        image_url = v['imageinfo'][0]['url']

    return image_url

def main():
    print(get_image_url())

if __name__ == '__main__':
    main()