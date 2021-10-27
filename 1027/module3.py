# https://note.nkmk.me/python-re-match-search-findall-etc/
import re

# 正規表現
s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

# 文字列の先頭がマッチするかチェック、抽出: match()
m = re.match(r'([a-z]+)@([a-z]+)\.com', s)
print("m：{}".format(m))

# 置換を行うre.sub()では第二引数に置換文字列、第三引数に処理対象の文字列を指定する。
result = re.sub(r'([a-z]+)@([a-z]+)\.com', 'new-address', s)
print("result：{}".format(result))