import os
import pickle
# while_word.py を pickle を利用したものに変更した


# osが、pythonscriptの中で動いてるから、直下にできてしまうのでファイルのパス指定する必要がある
DATA_FILENAME = '1117/word.txt'  
if os.path.isfile(DATA_FILENAME):   # ファイルがあるかどうかの確認
    # ここからファイルを読み込む
    with open(DATA_FILENAME,'rb') as file:  # 開いたファイルを「f」として扱う
        # 単語リストに格納
        a = pickle.load(file)
else:  # ファイルがないとき
    a = []



while True:
    wordinput = input('単語を入力してください：')
    # 空文字で終了
    if wordinput == "":
        print('終了します')
        break
    # LISTと打たれたらリストを表示
    if wordinput == "LIST":
        print(a)
        continue
    # 登録済みかどうか
    if wordinput in a:
        print("すでに登録済みです")
        continue
    # 登録済みじゃなければリストに追加
    else:
        a.append(wordinput)
# print('これまでに覚えた単語：{0}'.format(a))
print('これまでに覚えた単語：', a)
# ファイルに書き出す
with open(DATA_FILENAME,'wb') as file:
    pickle.dump(a,file)