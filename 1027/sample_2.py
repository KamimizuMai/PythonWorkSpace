fruits = ['バナナ','リンゴ','オレンジ']

while True:
    new = input("果物をカタカナで入力してください：")
    # 終了条件
    if new == '':
        break

    if new in fruits:
        print('{}は、知っています！'.format(new))
    else:
        print('{}は、知りませんでした。覚えておきます。'.format(new))
        # これだとできなかった
        # fruits[len(fruits)] = new

        # これだとできなかった
        # fruits += new

        # appendで末尾に追加、変な動きしたらf5で実行する
        fruits.append(new)

print('知っている果物')
print(fruits)
