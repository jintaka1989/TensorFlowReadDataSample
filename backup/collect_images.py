# -*- coding: utf-8 -*-

import sys
import urllib2

def download(url, path):
    try:
        # URLから画像を取得
        i = urllib2.urlopen(url)
        filename = url.split('/')[-1]

        # saveData というバイナリデータを作成
        saveData = open(path + filename, 'wb');

        # saveDataに取得した画像を書き込み
        saveData.write(i.read());
        saveData.close()

        print u'>>> get:' + filename
        i.close()
    except:
        print u'>>> error: ' + url

if __name__ == "__main__":

    download(sys.argv[1], sys.argv[2])
