# 10 else!
# 10 finish
a = 0
while a < 10:
    a += 1
    if a == 5:
        continue
# 偽になったとき、つまり10になったとき
else:   
    print(a, "else!")
print(a, "finish")
