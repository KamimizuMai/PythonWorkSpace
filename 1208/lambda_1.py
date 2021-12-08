my_list = [1, 3, 5, 7, 2, 4, 6, 8]

#list
#受け取った意イミテータを基にリストを作成する
#map
#繰り返し処理をシンプルに
# 加工元となる値群を第二引数に指定し、それをどのように加工するのかというところが第一引数によって指定

new_list = list(map(lambda x: x*10,my_list))
print(my_list)
print(new_list)
