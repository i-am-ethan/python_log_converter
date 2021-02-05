# -*- coding: utf-8 -*-

# 入力ファイルの定義
stablepath = '/Users/ethan/Desktop/log_converter/photon_converter/before_logs/'
# before_logs配下のconvertしたいtxtファイルを下に指定する
changepath = 'photon_converter.txt'
# テキストファイルの中身をリストとして取得
path = stablepath + changepath

# テキストファイル をリスト化する
with open(path) as f:
    lines = f.readlines()

# 行の中身を抽出する
lines_strip = [line.strip() for line in lines]

# keywordsが含まれた行を抽出する
keywords1 = 'Send [SC1_START]'
keywords2 = 'Send [BANZAI_OK]'

l_log21 = [line for line in lines_strip if (
    keywords1 in line) or (keywords2 in line)]

for line in l_log21:
    print(line)

# 結果をテキストファイルに出力する
with open('/Users/ethan/Desktop/log_converter/photon_converter/converted_logs/photon_converted.txt', 'wt') as d:
    for line in l_log21:
        d.write(line+'\n')
