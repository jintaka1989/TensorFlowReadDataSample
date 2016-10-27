#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 実行方法
# コマンドラインから下記のようにして実行する．
# ただし，引数dirはget_IMGを用いない(画像を保存しない)場合は指定しない．
# collect_img.py
# $ python collect_img.py query dir
# query: 欲しい画像の検索ワード (e.g. leopard)
# dir: 画像保存先ディレクトリ (./img/*)

import sys
import os
import re
import commands as cmd
import pdb


# クエリ検索したHTMLの取得
def get_HTML(query):

    html = cmd.getstatusoutput("wget -O - https://www.bing.com/images/search?q=" + query)

    return html

# jpg画像のURLを抽出
def extract_URL(html):

    url = []
    sentences = html[1].split('\n')
    # ptn = re.compile('<a href="(.+\.jpg)" class="thumb"')
    ptn = re.compile('href="(.*?).jpg')



    for sent in sentences:
        sents = sent.split('div class=')
        for s in sents:
            search = re.search(ptn, s)
            if search is None:
                print 'Not match'
            else:
                print search.group(1)
                url.append(search.group(1)+".jpg")

    return url

# ローカルに画像を保存
def get_IMG(dir,url):

    for u in url:
        try:
            os.system("wget -P " + dir + " " + u)
        except:
            continue


if __name__ == "__main__":

    argvs = sys.argv # argvs[1]: 画像検索のクエリ, argvs[2]: 保存先のディレクトリ(保存したい時のみ)
    query = argvs[1] # some images  e.g. leopard

    html = get_HTML(query)

    url = extract_URL(html)

    for u in url:
        print u

    # 画像をローカルに保存したいときに有効にする
    get_IMG(argvs[2],url)
