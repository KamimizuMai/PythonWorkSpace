
import re
DATA_FILENAME = "1124/sentence.txt"

with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    dict1 = {}  # 空の辞書を作成

    for line in f:
        # いらないもの取り除いて配列に
        # re.sub(いらない記号,置き換える文字,置き換えられる文字)
        # 配列に入れる文字.split(区切り文字) 区切り文字はデフォルトでは空白
        words = re.sub(r'[",.:()]',' ',line.strip().lower()).split()

        for word in words:
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
        print(dict1)
        # dict1 = remove_null(dict1)
len_max = 0
for word in dict1.keys():
    len_max = max(len_max,len(word))
for key in sorted(dict1):
    print(f"{key:{len_max}}:{dict1[key]}")