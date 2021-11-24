
while True:
    nyuryoku = int(input("整数を入力してください(終了->):"))
    if nyuryoku == 0:
        break
    elif nyuryoku%2==0:
        print("偶数です。")
    else:
        print("奇数です。")
