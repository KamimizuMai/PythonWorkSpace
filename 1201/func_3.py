# 受け取った値は、タプル型となる。
# a1,a2 = args のように別々の変数に格納できる。
# args[0]のように使用しても良い。
def do_anything(*args):
    if len(args) == 0:
        print("やることないので暇です")
    elif len(args) == 1:
        # args[0]じゃなくargsだとタプル型で入っちゃう
        args1 = args[0]
        print(type(args1))
        if type(args1) != int and type(args1) != str:
            print("難しくて無理です")
        else:
            print(args1*2)

    elif len(args) == 2:
        args1, args2 = args
        print(type(args1))

        if type(args1) == type(args2) != int and type(args1) == type(args2) != str:
            print("無茶言わないで！")
        elif type(args1) != type(args2):
            print("できません～")
        else :
            print(args1+args2)
    else:
        print("無理です...")


print("受け取った値：(10,)")

do_anything(10)
