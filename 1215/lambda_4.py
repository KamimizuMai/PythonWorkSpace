import random
# 初期化
marks = ('S','H','C','D')   #マーク
cards = []                  #デッキ用リスト


for m in marks:
 for n in range(1,14):
    t = (m,n) # タプルでカード生成
    cards.append(t) # リストに追加

# 5 枚選択

# ランダムに要素を一つ選択: random.choice()
# ランダムに複数の要素を選択（重複なし）: random.sample()
# ランダムに複数の要素を選択（重複あり）: random.choices()
select_cards = random.sample(cards,5)

# 並び替え
# p180
# 降順にソートしたい場合は引数reverseをTrueとする
select_cards.sort(reverse = True,key=lambda x:x[1])

# 出力

print(select_cards)