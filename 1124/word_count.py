# 途中
DATA_FILENAME = "1124/word_list.txt"

dict1 = {}  # 空の辞書を作成
with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()  # 改行コードを取り除く
        # https://note.nkmk.me/python-dict-in-values-items/
        if line in dict1:  # 辞書のキーに単語が存在するか？
            dict1[line] += 1  # カウントアップ
        else:
            dict1[line] = 1

print(dict1)

print("=*"*10)

# https://techacademy.jp/magazine/19309
# dict2 = dict(sorted(dict1.items()))

len_max = 0
for word in dict1.keys():       #キーを取り出す
    len_max = max(len_max,len(word))    #最大文字数を調べてる
for key in sorted(dict1):
    print(f"{key:{len_max}}:{dict1[key]}")