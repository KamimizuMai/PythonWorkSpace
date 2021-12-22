list_calc = []
kigou = True
# kigou = ['+','-','*','/']
while True:
    s = input("calc:")
    if s == '':
        break
    elif s == '=':
        break
    elif kigou == True and s.isnumeric():
        list_calc.append(s)
        kigou = False
    elif kigou == False and s in ['+', '-', '*', '/']:
        list_calc.append(s)
        kigou = True
    else:
        print("入力が正しくありません")
        continue
formula = ''.join(list_calc)  # 文字列を結合
print(f'入力した計算式:{formula}\n計算結果:{eval(formula)}')
# eval() 文字列を式として評価

# if list_calc
# print(list_calc[-1])
# if s == '=':
#     print(f"入力した値:{list_calc}")
#     break
# elif s in kigou:
#     list_calc.append(s)
# elif s.isnumeric():
#     list_calc.append(int(s))
# else :
#     print("入力が正しくありません")
