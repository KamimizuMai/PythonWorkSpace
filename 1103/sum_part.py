num1 = int(input("数字1："))
num2 = int(input("数字2："))
# 宣言だけしておく
sum = 0
for i in range(num1,num2+1):
    sum += i
print(f"{num1}から{num2}までの合計は{sum}です")