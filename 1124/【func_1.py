def combine_list(list1, list2):
    '''2 つのリストを結合し、リストで返す'''

    # これでもいける
    # if (type(list1) == list) and (type(list2) == list) :
    # andの代わりに&&は使えない
    if type(list1) is list and type(list2) is list :
        return list1 + list2
    else:
        print("引数がリストではありません")
        list3 = [list1,list2]
        return list3

# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))
