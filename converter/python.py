# -*- coding: utf-8 -*-

# 入力ファイルの定義
stablepath = './before_logs/'

# before_logs配下のconvertしたいtxtファイルを下に指定する
pathNum = 1
changepath = 'example' + str(pathNum) + '_converted.txt'

# テキストファイルの中身をリストとして取得
path = stablepath + changepath

# テキストファイル をリスト化する
with open(path) as f:
    lines = f.readlines()

# 行の中身を抽出する
lines_strip = [line.strip() for line in lines]

# keywordsが含まれた行を抽出する（キーワードを増やしたかったら足してください）
keywords1 = 'did'
keywords2 = 'TOM'
keywords3 = 'shouted'
# keywords4 = ''
# keywords5 = ''
# keywords6 = ''
# keywords7 = ''
# keywords8 = ''
# keywords9 = ''
# keywords10 = ''
# keywords11 = ''
# keywords12 = ''

# こちらも同じく
l_log21 = [line for line in lines_strip if (
    keywords1 in line) 
    or (keywords2 in line) 
    or (keywords3 in line) 
    # or (keywords4 in line) 
    # or (keywords5 in line) 
    # or (keywords6 in line) 
    # or (keywords7 in line) 
    # or (keywords8 in line) 
    # or (keywords9 in line) 
    # or (keywords10 in line) 
    # or (keywords11 in line) 
    # or (keywords12 in line)
    ]

for line in l_log21:
    print(line)

# convert後の設定
with open('./converted_logs/example' + str(pathNum) + '_converted.txt', 'wt') as d:
    for line in l_log21:
        d.write(line+'\n')
