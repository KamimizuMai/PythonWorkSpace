# https://note.nkmk.me/python-str-num-determine/

while True:
    str = input("好きな文字を入力してください：")

    # 空文字入力でループでる
    if str == "" :
        break

    # 数字かどうか
    # isdigit()でもいい
    if str.isnumeric():
        print("数字")
    # アルファベットかどうか
    elif str.isalpha():
        print("アルファベット")
    else:
        print("その他")
