# 空のリスト作成
array = []

while True:
    str = input("単語を入力してください：")
    # 空文字で終了
    if str == "":
        print("終了します")
        break
    # LISTと打たれたらリストを表示
    if str == "LIST":
        print(f"{array}")
        continue
    # 登録済みかどうか
    if str in array:
        print("すでに登録済みです")
    # 登録済みじゃなければリストに追加
    else:
        array.append(str)
print("これまでに覚えた単語：{0}".format(array))
