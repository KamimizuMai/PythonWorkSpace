import datetime

def log_file(func):
    def funcname(*args, **kwargs):
        # ファイルを使用します
        DATA_FILENAME = '1222/python.log'
        dt_now = datetime.datetime.now()
        print("log_fileだよ")

        # 追記なので'a'
        with open(DATA_FILENAME, 'a') as f:
            # 書き方
            # func.__name__は受け取った関数名
            f.write(f'{dt_now}function:{func.__name__} args:{args} kwargs:{kwargs}\n')

            
            
        result = func(*args,**kwargs)
        return result
    return funcname
# main


@log_file
def test(n):
    print('test->{}'.format(n))


# 呼出
# @log_fileがあるので、test呼び出すだけじゃなくてlog_fileにも飛ぶ
# testの前にlog_file通ってる
test(100)
# 呼出
for i in range(5):
    test(i)
