# インポート
from time import sleep
hiki = None
while True:
    hiki = int(input("何匹数えますか？："))
    if hiki <= 100:
        break
    print("多すぎます")

for i in range(1,hiki+1):
    # 一定時間何もしない
    sleep(0.5+0.025*i)
    print(f"羊が{i}匹")