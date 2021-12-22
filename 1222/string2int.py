def str2int(moji):
    if type(moji) is str :      #この行ないとエラーでた
        if moji.isnumeric():
            return int(moji)
        else:
            return 0
    return moji



print(str2int('a'))
print(str2int('10'))
print(str2int(100))


