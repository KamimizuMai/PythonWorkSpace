# 整数を入力してください：5
n= input("整数を入力してください：")

# rangeについて
# https://www.javadrive.jp/python/function/index6.html
array = range(1,int(n)+1)
sum = sum(array)
# 1~5までの合計：15
print(f"1~{n}までの合計：{sum}")
# 平均：3.0
print("平均：{0}".format(sum/int(n)))

# formatのやり方色々『101304/basic.py』
# https://gammasoft.jp/blog/python-string-format/
