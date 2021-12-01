# あらかじめ、初期値を設定(tax=10)
def tax_included(price, tax=10):
    if tax<0:
        return None
    # /が優先される。1必須
    return int(price * (1+tax / 100))

# 5000の税込み金額は5500円
print('{}の税込み金額は{}円'.format(5000, tax_included(5000)))
# 5000の消費税8%の税込み金額は5400円
print('{}の消費税{}%の税込み金額は{}円'.format(5000, 8, tax_included(5000, 8)))

print('{}の消費税{}%の税込み金額は{}円'.format(5000, -10, tax_included(5000, -10)))
