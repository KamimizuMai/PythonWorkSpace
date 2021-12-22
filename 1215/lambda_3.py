my_list = ['hello', 'nice', 'abc', 'test', 'morning', 'good', 'yes', 'world']

# filter()は第一引数の処理の結果がTrueと判定される要素を抽出する。
new_list = list(filter(lambda s: len(s) >= 5, my_list))
print(my_list)
print(new_list)


# list リストを作成
# map  リストを作成する際、関数を適用
# filter リストを作成する際、条件で抽出