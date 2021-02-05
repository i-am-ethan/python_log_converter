# -*- coding: utf-8 -*-

# 入力ファイルの定義
stablepath = '/Users/ethan/Desktop/log_converter/phone_converter/before_logs/'
# before_logs配下のconvertしたいtxtファイルを下に指定する
# changepath = 'phone1_converted.txt'
# changepath = 'phone2_converted.txt'
# changepath = 'phone3_converted.txt'
# changepath = 'phone4_converted.txt'
# changepath = 'phone5_converted.txt'
changepath = 'phone6_converted.txt'
# テキストファイルの中身をリストとして取得
path = stablepath + changepath

# テキストファイル をリスト化する
with open(path) as f:
    lines = f.readlines()

# 行の中身を抽出する
lines_strip = [line.strip() for line in lines]

# keywordsが含まれた行を抽出する
keywords1 = 'Get [SC1_START]'
keywords2 = 'Movie Request[1]'
keywords3 = 'Movie Received[1]'
keywords4 = 'Request[20]'
keywords5 = 'Received[20]'
keywords6 = 'Request[21]'
keywords7 = 'Received[21]'
keywords8 = 'Get [BANZAI_OK]'
keywords9 = 'Movie Request[30]'
keywords10 = 'Movie Received[30]'
keywords11 = 'START GESTURE'
keywords12 = 'playerEffectRPC'

l_log21 = [line for line in lines_strip if (
    keywords1 in line) or (keywords2 in line) or (keywords3 in line) or (keywords3 in line) or (keywords5 in line) or (keywords6 in line) or (keywords7 in line) or (keywords8 in line) or (keywords9 in line) or (keywords10 in line) or (keywords11 in line) or (keywords12 in line)]

for line in l_log21:
    print(line)

# 結果をテキストファイルに出力する
# with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone1_converted.txt', 'wt') as d:
#     for line in l_log21:
#         d.write(line+'\n')

# with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone2_converted.txt', 'wt') as d:
#     for line in l_log21:
#         d.write(line+'\n')

# with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone3_converted.txt', 'wt') as d:
#     for line in l_log21:
#         d.write(line+'\n')

# with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone4_converted.txt', 'wt') as d:
#     for line in l_log21:
#         d.write(line+'\n')

# with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone5_converted.txt', 'wt') as d:
#     for line in l_log21:
#         d.write(line+'\n')

with open('/Users/ethan/Desktop/log_converter/phone_converter/converted_logs/phone6_converted.txt', 'wt') as d:
    for line in l_log21:
        d.write(line+'\n')
