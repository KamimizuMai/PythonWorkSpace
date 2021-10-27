# 後で使うために空の変数用意
# ただの変数名だけだとエラー出る
seisu = None

while seisu != 0:
    # 数字を入れるときinputはintで囲むこと忘れずに！！！
    seisu = int(input("整数を入力してください(終了->0) ："))
    if seisu % 2 == 0:
        print("偶数です。")
    else:
        print("奇数です。")


# 板書
while True:
    n = int(input("整数を入力してください(終了->0) ："))
    if n == 0:
        # while 文や for 文のブロックの中で break 文が実行されると繰り返し処理が強制的に終了
        break
    if seisu % 2 == 0:
        print("偶数です。")
    else:
        print("奇数です。")