def str2int(moji):
    # '''で囲むと関数の説明が書ける。関数にカーソル合わせると出る
    # 複数行で関数の説明書くときは"""で囲む
    """str2int
    文字列を数値（整数）に変換して、値を返す。
    変換できない場合は 0 を返す
    文字列でない場合は、そのまま値を返す。
    """
    if type(moji) is str: #文字かどうか確認
        if moji.isnumeric(): #数値かどうかの確認
            return int(moji) #true
        else:
            return 0 
    else:
        return moji

print(str2int('a'))
print(str2int('10'))
print(str2int(100))


