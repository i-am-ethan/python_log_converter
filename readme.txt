■log_converterをなぜつくったか
・膨大な量のログの中から、文字検索をして任意の行を抽出したかった。

■使い方
(0)結合.txtファイルをつくる。
まず最初に、大量にある.txtファイルを1つの.txtファイルに結合する。
// 任意のディレクトリにいく
$ cat *.txt>photon_converted.txt
↑ 現在いるディレクトリ配下の.txtを結合して、photon_converter.txtを作成する

(1)photon_converted.txtを'photon_converter/before_logs/'配下におく。
(2)keywordsを設定する
(3)python python.pyを実行する

(4)photon側も同じ
catコマンド
cat *.txt > phone1_converted.txt
cat *.txt > phone2_converted.txt
cat *.txt > phone3_converted.txt
cat *.txt > phone4_converted.txt
cat *.txt > phone5_converted.txt
cat *.txt > phone6_converted.txt