# 仮引数の先頭に「**」をつけることで、キーワード引数を辞書としてまとめることが可能
# args と kwargs を併用する場合は、順番に注意
def say_dic(word, *args, **kwargs):
    print(word)
    print(args)
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


say_dic('hello', 'Mike', 1, desert='banana', drink='beer')

# 辞書にしてから渡す方法
t = {'math': 15, 'science': 100}
# **つけて渡す
say_dic('hi', 'Nancy', 2, **t)
