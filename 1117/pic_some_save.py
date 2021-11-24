import pickle
a = 10
b = 'abc'
c = '漢字'
with open('1117/pics.pkl', 'wb') as f:
    pickle.dump([a, b, c], f)
