# log_converter をなぜつくったか

・膨大な量のログの中から、文字検索をして任意の行を抽出したかった。

例えば、web サーバーなどのログは大量に生成されて、後々その中から任意の行を抽出するときになどに使う。

# 推奨環境

私は Mac user なので、基本的には MacOS であれば動くと思います。
terminal をつかったコマンドを使うので他の OS だと多少異なるかもしれません。
python のバージョンは：”Python 2.7.17”です。

# 使い方

(1)結合.txt ファイルをつくる。
まず最初に、大量に生成されたログ(.txt)ファイルを
1 つの.txt ファイルに結合しちゃいます。

// 任意のディレクトリ(デスクトップ)にいく
$ cd Desktop
// cat コマンド。全ての(.txt)ファイルを結合するコマンド
$ cat \*.txt>example1_converted.txt
※example1_converted.txt は任意の名前を設定します。
ただし後々、python のプログラム側でも変更が必要です。

(2)example1_converted.txt を'converter/before_logs/'配下におく。
先ほど cat で結合したテキストファイル を before_logs においてください。

(3)keywords を設定する
キーワードが含まれた行を抽出するためのキーワードを python ファイルないで設定してください。
デフォルトだと 14 個まで設定可能です。
14 個以上設定したい場合も、コードをみてもらえれば簡単に増やせると思います。

(4)python python.py を実行する
python.py ファイルがあるところまで移動して python.py を実行します。
すると、converted\*logs 直下に example1_converted というファイルが生成されます。
ファイル名は python ファイル内で変更可能です。

# ちょっとだけ応用？

なにかのログをとるとなると、1 つのサーバーや 1 つの端末だけではなく、複数のサーバーや端末のログを抽出することになると思います。

その際はあ対応できるように path の変数を変えてあげてください。

# 参考文献：

① 無料で小説が読める青空文庫：Project Gutenberg
http://www.gutenberg.org/ebooks/74
題名：トムソーヤの冒険 - マーク・トウェイン（The Adventure of Tom Sawyer - Mark Twain）

②Python でファイル内の任意の文字列を含む行を抽出（grep 的処理）
https://note.nkmk.me/python-grep-like/

③[python]encoding error
https://qiita.com/e_san_desuyo/items/4be39d3460e8f635ae34
