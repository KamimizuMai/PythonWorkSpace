# 関数を辞書で渡し、実行する
def func1():
    print("Hello")


def func2():
    print("Goodbye")


# main
run_list = {'a': func1, 'b': func2}


while True:
    print("a=>Hello,b=>Goodbye")
    n = input("どちらを実行しますか？")

    if n == '':     #入力された文字が空文字だった時
        break

    # for funckey, funcval in run_list.items():
    #     if n == funckey:
    #         funcval()

    if n in run_list.keys():    #run_listのkeyに入力値が存在する場合
        run_list[n]()
    else:
        print("どちらかを選択してください")