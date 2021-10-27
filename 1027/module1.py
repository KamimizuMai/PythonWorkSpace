# asで別名指定してみた
import random as rand
# https://docs.python.org/ja/3.8/library/random.html


# 0~9まで繰り返し
for i in range(10):
    # 0から4までのランダムな整数を表示
    num = rand.randrange(0, 5)
    print(num)
