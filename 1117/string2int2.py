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

def list2int(moji):
    # '''で囲むと関数の説明が書ける。関数にカーソル合わせると出る
    # 複数行で関数の説明書くときは"""で囲む
    """
    list2int 文字列を数値に変換した値を返す（List 対応）
    """
    if type(moji) is str:#文字列か？
        return str2int(moji)
    elif type(moji) is list: #リストかどうか
        result =[]
        for i in moji:
            result.append(str2int(i))
        return result
        
    else:
        return None

print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))


