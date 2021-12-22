import math


def input_int(message):
    """messageを表示 入力値(int)を返す"""
    value = input(f"{message}を入力してください：")
    if value.isnumeric():
        value = int(value)
    else:
        value = 0
    return value


def calc_payment(total, num_people):
    """合計金額と人数から金額を計算する。戻り値は、参加者の金額と漢字の金額をリストで返す"""
    pay_people = total/num_people
    pay_people = math.ceil((pay_people/100)*100)
    pay_coodinator = total - pay_people * (num_people-1)

    return [pay_people, pay_coodinator]


def output_payment(pay_people,pay_coodinator,num_people):
    """
    参加者の支払金額、幹事の支払金額
    参加人数を書式化して出力(戻り値なし)
    """

    print(f"支払金額：{pay_people}円 ({num_people}人)")
    print(f"幹事金額：{pay_coodinator}円")


# main
total = input_int('支払合計金額')
num_people = input_int('参加者人数')

[pay_people,pay_coodinator] = calc_payment(total,num_people)

output_payment(pay_people,pay_coodinator,num_people)