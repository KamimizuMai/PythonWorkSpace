import pickle
big_num = 2**100
with open('1117/bignum.pkl', 'wb') as f:
    pickle.dump(big_num, f)
