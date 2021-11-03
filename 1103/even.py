# 【実行例１】
print("偶数一覧")
for i in range(1,100) :
    if (i % 2) == 0 :
        # 改行させない
        print(i,end=",")

print("\n"+"=-"*20)

# 【実行例2】(力技)
print("偶数一覧=>[",end="")
for i in range(1,100) :
    if (i % 2) == 0 :
        # 改行させない
        print(i,end="")
        if i == 98 :
            continue
        else :
            print(",",end="")
print("]")


print("\n"+"=-"*20)

# 【実行例2】
# 板書
result = []
for i in range(1,100):
    if i % 2 == 0:
        result.append(i)
print(f"偶数一覧=>{result}")



